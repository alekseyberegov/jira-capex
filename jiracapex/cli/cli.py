import os
import sys
import click
import json
from sqlalchemy import create_engine

from jiracapex.conf.config_loader import ConfigLoader
from jiracapex.api.jira_endpoint import Endpoint
from requests.auth import HTTPBasicAuth
from typing import Dict
from os.path import exists, expanduser, join

CONTEXT_SETTINGS = dict(auto_envvar_prefix="jiracapex")

class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.__config = (ConfigLoader("jiracapex.ini")).config()
        self.__client = self.settings()

    def auth(self) -> HTTPBasicAuth:
       return HTTPBasicAuth(self.__config.get('auth', 'user'), self.__config.get('auth', 'token'))

    def endpoint(self, name: str) -> Endpoint:
       return Endpoint(self.config('jira', name), self.auth())

    def engine(self):
        return create_engine('sqlite:///' + self.__client['db'])

    def config(self, section: str, option: str) -> str:
        return self.__config.get(section, option)

    def settings(self) -> Dict:
        data = None
        file = join(expanduser("~"), '.jiracli.json')
        if (exists(file)):
            with open(file, 'r') as fd:
                data = json.load(fd)
        
        return data if data is not None else {'version': 1}

    def save(self, settings: Dict):
        file = join(expanduser("~"), '.jiracli.json')
        with open(file, 'w', encoding ='utf8') as fd:
            json.dump(settings, fd)

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))

class JiraCLI(click.MultiCommand):
    def list_commands(self, ctx):
        cmds = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                cmds.append(filename[4:-3])
        cmds.sort()
        return cmds

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"jiracapex.cli.commands.cmd_{name}", None, None, ["cli"])
        except ImportError as e:
            raise e
        return mod.cli


@click.command(cls=JiraCLI, context_settings=CONTEXT_SETTINGS)
@click.option(
    "--home",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    help="Changes the folder to operate on.",
)
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@pass_environment
def cli(ctx, verbose, home):
    """jira command line interface."""
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home

if __name__ == '__main__':
    cli()