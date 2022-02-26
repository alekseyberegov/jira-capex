import click, json
from typing import Dict
from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_changelog import JiraChangelog
from jiracapex.json.utils import flatten_json

@click.command("changelog", short_help="shows changelog")
@click.argument("issue_id") 
@click.option('--start-at', default=0, show_default=True)
@click.option('--max-results', default=1, show_default=True)
@pass_environment
def cli(ctx, issue_id, start_at: int = 0, max_results: int = 1):
    changelog: JiraChangelog = JiraChangelog(ctx.endpoint('changelog_url'))
    resp = changelog.query(issue_id, start_at, max_results)
    for rec in resp['values']:
        change:Dict[str,str] = flatten_json(rec)
        ctx.log(json.dumps(change, sort_keys=True, indent=4, separators=(",", ": "))) 
