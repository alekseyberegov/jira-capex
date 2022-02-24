import click, json

from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch
from jiracapex.orm.dyna_object import DynaObject
from sqlalchemy import create_engine
from typing import Dict

@click.command("load", short_help="load data into database using JQL")
@click.argument("query") 
@click.option('--map')
@click.option('--start_at', default=0, show_default=True)
@click.option('--max_results', default=1, show_default=True)
@pass_environment
def cli(ctx, query, map, start_at, max_results):
    conf: Dict = ctx.settings()
    dyna_obj: DynaObject = DynaObject(map)
    dyna_obj.bind(create_engine('sqlite:///' + conf['db'])).create_table()
    search: JiraSearch = JiraSearch(ctx.config('jira', 'search_url'), ctx.auth())
    search.set_fields(list(dyna_obj.nodes()))
    resp = search.query(query, start_at=start_at, max_results=max_results)
    for r in resp['issues']:
        dyna_obj.add(r)
    dyna_obj.flush()

