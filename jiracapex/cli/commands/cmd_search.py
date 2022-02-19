import click, json

from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch

@click.command("search", short_help="query Jira using JQL")
@click.argument("query") 
@pass_environment
def cli(ctx, query):
    search: JiraSearch = JiraSearch(ctx.config('jira', 'search_url'), ctx.auth())
    search.set_fields(["summary", "status", "assignee", "created", "creator"])
    resp = search.query(query)

    ctx.log(json.dumps(resp, sort_keys=True, indent=4, separators=(",", ": ")))
