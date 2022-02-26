import click
from typing import Dict, List
from jiracapex.cli.cli import pass_environment
from jiracapex.api.jira_search import JiraSearch
from jiracapex.json.utils import flatten_json
from jiracapex.orm.default_mapping import DEFAULT_FIELD_MAPPING, BLOCKED_FIELDS

@click.command("schema", short_help="generate schema")
@click.argument("key") 
@click.option('--no-nulls', is_flag=True)
@click.option('--filter')
@pass_environment
def cli(ctx, key, no_nulls, filter):
    search: JiraSearch = JiraSearch(ctx.endpoint('search_url'))
    search.set_fields(["-all"])
    resp = search.query(f"key={key}", start_at=0, max_results=1)
    for rec in resp['issues']:
            issue:Dict[str,str] = flatten_json(rec)
            for key, value in issue.items():
                if key.find('icon') == -1 \
                     and key.find('avatar') == -1 \
                         and key.find('color') == -1 \
                            and key not in BLOCKED_FIELDS:
                    col = DEFAULT_FIELD_MAPPING.get(key, suggest_column(key))
                    if value is not None or not no_nulls:
                        if filter is None or key.find(filter) != -1:
                            ctx.log("'" + key + "': " + "'"+ col +"', # " + str(value)) 

def suggest_column(key: str) -> str:
    parts: List = key.split('_')
    if len(parts) > 1:
        out = "_".join(parts[1:])
    else:
        out = key
    return out
