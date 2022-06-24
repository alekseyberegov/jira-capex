import click
from jiracapex.cli.cli import pass_environment, Environment
from jiracapex.reporting.report import Report

@click.command("sql", short_help="run SQL script")
@click.argument("sqlfile", type=click.Path(exists=True))
@click.option('--param',  multiple=True, type=(str, str))
@pass_environment
def cli(ctx: Environment, sqlfile, param):
    sql_params = {}
    if param is not None:
        for name, value in param:
            sql_params[name] = value

    with open(sqlfile, 'r') as reader:
        sql_query = reader.read()

    report = Report(ctx.engine())
    report.run(sql_query, sql_params)
    
    print(report.df.dtypes)
    print(report.df)