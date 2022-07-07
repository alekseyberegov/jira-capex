import click
from pandas import DataFrame
from jiracapex.cli.cli import pass_environment, Environment
from jiracapex.reporting.runner import ReportRunner, Report
from jiracapex.reporting.runner import ReportContext

@click.command("report", short_help="run the report")
@click.argument("name", type=str)
@click.option('--param',  multiple=True, type=(str, str))
@click.option('--cols',  is_flag=True)
@pass_environment
def cli(ctx: Environment, name, param, cols):
    context: ReportContext = ReportContext()
    context['project_home'] = ctx.home
    if param is not None:
        for n, v in param:
            context[n] = v

    runner = ReportRunner(ctx.engine())
    df: DataFrame = runner.run(Report.new_instance(name, context))
    if cols: print(df.dtypes)
    print(df)



