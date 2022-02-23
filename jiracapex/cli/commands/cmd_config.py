import click, json
from jiracapex.cli.cli import pass_environment

@click.command("config", short_help="configure the environment")
@click.argument("command", type=click.Choice(['db', 'show'], case_sensitive=False))
@click.argument("value", default="")
@pass_environment
def cli(ctx, command, value):
    conf = ctx.settings()

    if command == 'show':
        ctx.log(json.dumps(conf, sort_keys=True, indent=4, separators=(",", ": ")))
    elif command == 'db':
        conf['db'] = value
        ctx.save(conf)


