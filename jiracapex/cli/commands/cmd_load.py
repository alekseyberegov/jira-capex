import click, json

from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch
from jiracapex.orm.dyna_object import DynaObject
from sqlalchemy import create_engine
from typing import Dict

@click.command("load", short_help="load data into database using JQL")
@click.argument("query") 
@click.option('--map')
@click.option('--max_results', default=1, show_default=True)
@click.option('--batch_size', default=100, show_default=True)
@pass_environment
def cli(ctx, query, map, max_results, batch_size):
    conf: Dict = ctx.settings()
    dyna_obj: DynaObject = DynaObject(map)
    dyna_obj.bind(create_engine('sqlite:///' + conf['db'])).create_table()

    search: JiraSearch = JiraSearch(ctx.config('jira', 'search_url'), ctx.auth())
    search.set_fields(list(dyna_obj.nodes()))

    start_at: int = 0
    while start_at < max_results:
        resp = search.query(query, start_at=start_at, max_results=batch_size)
        cnt: int = 0
        for r in resp['issues']:
            dyna_obj.add(r)
            cnt += 1
        dyna_obj.flush()
        if cnt < batch_size:
            break
        start_at += cnt


