import click, json

from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch
from jiracapex.json.utils import flatten_json

# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-post

@click.command("search", short_help="query Jira using JQL")
@click.argument("query") 
@click.option('--start_at', default=0, show_default=True)
@click.option('--max_results', default=1, show_default=True)
@click.option('--flatten', is_flag=True)
@pass_environment
def cli(ctx, query, start_at, max_results, flatten):
    search: JiraSearch = JiraSearch(ctx.config('jira', 'search_url'), ctx.auth())
    search.set_fields(["-all"])
    resp = search.query(query, start_at=start_at, max_results=max_results)

    def truncate(s: str, width: int=60) -> str:
        return s[:width] if len(s) > width else s

    if flatten:
        for rec in resp['issues']:
            obj = flatten_json(rec)
            ctx.log('-' * 60 + '+' + '-' * 60)
            for key, value in obj.items():
                ctx.log("{0:<60}|{1:60}".format(key, truncate(str(value))))
    else:
        ctx.log(json.dumps(resp['issues'], sort_keys=True, indent=4, separators=(",", ": ")))
