import click, json
import pandas as pd 

from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch

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

    if flatten:
        issues_df = pd.json_normalize(resp, record_path =['issues'], sep='_')
        with pd.option_context('display.max_rows', 5, 'display.max_columns', 2): 
            print(issues_df)
    else:
        ctx.log(json.dumps(resp['issues'], sort_keys=True, indent=4, separators=(",", ": ")))
