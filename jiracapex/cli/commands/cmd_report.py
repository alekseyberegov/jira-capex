import click
from pandas import DataFrame
from jiracapex.cli.cli import pass_environment, Environment
from jiracapex.reporting.runner import ReportRunner, Report
from jiracapex.reporting.runner import ReportContext

@click.command("report", short_help="run the report")
@click.argument("name", type=str)
@click.option('--param',  multiple=True, type=(str, str))
@pass_environment
def cli(ctx: Environment, name, param):
    context: ReportContext = ReportContext()
    context['project_home'] = ctx.home
    if param is not None:
        for n, v in param:
            context[n] = v

    runner = ReportRunner(ctx.engine())
    df: DataFrame = runner.run(Report.new_instance(name, context))
    print(df.dtypes)    
    print(df)



