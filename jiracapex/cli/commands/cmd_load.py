import click, json
from datetime import date, datetime
from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch
from jiracapex.orm.dyna_object import DynaObject
from sqlalchemy import create_engine
from typing import Dict

@click.command("load", short_help="load data into database using JQL")
@click.argument("query") 
@click.option('--map')
@click.option('--max-results', default=1, show_default=True)
@click.option('--batch-size', default=100, show_default=True)
@click.option('--no-save', is_flag=True)
@pass_environment
def cli(ctx, query, map, max_results, batch_size, no_save):
    conf: Dict = ctx.settings()
    dyna_obj: DynaObject = DynaObject(map)
    dyna_obj.bind(create_engine('sqlite:///' + conf['db'])).create_table()

    search: JiraSearch = JiraSearch(ctx.endpoint('search_url'))
    search.set_fields(list(dyna_obj.nodes()))

    start_at: int = 0
    while start_at < max_results:
        resp = search.query(query, start_at=start_at, max_results=batch_size)
        cnt: int = 0
        if 'issues' not in resp:
            ctx.log(resp)
            break;

        for r in resp['issues']:
            dyna_obj.add(r)
            cnt += 1
        if no_save:
            for o in dyna_obj.cached():
                ctx.log(json.dumps(o, sort_keys=True, indent=4, separators=(",", ": "), default=json_serial))
            dyna_obj.clear()
        else:
            dyna_obj.flush()
        if cnt < batch_size:
            break
        start_at += cnt

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
