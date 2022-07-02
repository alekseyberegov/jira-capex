import click
from jiracapex.cli.cli import pass_environment, Environment
from jiracapex.reporting.runner import ReportRunner
from jiracapex.reporting.runner import ReportContext

@click.command("report", short_help="run the report")
@click.argument("name", type=str)
@click.option('--param',  multiple=True, type=(str, str))
@pass_environment
def cli(ctx: Environment, name, param):
    context: ReportContext = ReportContext()
    if param is not None:
        for n, v in param:
            context.set_arg(n, v)

    context.set_var('project_home', ctx.home)
    report = ReportRunner(ctx.engine())
    report.run_report(name, context)

    print(report.df)



