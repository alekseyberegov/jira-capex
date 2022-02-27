import click, json
from typing import Dict
from sqlalchemy import create_engine
from jiracapex.orm.dyna_object import DynaObject
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
    if issue_id == 'all':
        conf: Dict = ctx.settings()
        engine = create_engine('sqlite:///' + conf['db'])

        issue_obj: DynaObject = DynaObject('map_issue')
        issue_obj.bind(engine).create_table()
        ids = []
        for i in issue_obj.get_primary_keys():
            ids.append(i)
       

        change_obj: DynaObject = DynaObject('map_changelog')
        change_obj.bind(engine).create_table()
        loaded_ids = {}
        for i in change_obj.get_primary_keys(column='issue_id'):
            loaded_ids[str(i)] = True
 
        cnt:int = 0
        for i in ids:
            cnt += 1
            if str(i) in loaded_ids:
                ctx.log(f"[{cnt}] Skipping issue {i}; History is already loaded")
            else:    
                ctx.log(f"[{cnt}] Storing history for issue {i}")
                resp = changelog.query(i, start_at, max_results)
                for r in resp['values']:
                    o = dict(r)
                    o['issue_id'] = i
                    change_obj.add(o)
                change_obj.flush()
    else:
        resp = changelog.query(issue_id, start_at, max_results)
        for rec in resp['values']:
            change:Dict[str,str] = flatten_json(rec)
            ctx.log(json.dumps(change, sort_keys=True, indent=4, separators=(",", ": "))) 
