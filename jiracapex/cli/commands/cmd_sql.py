import click
from jiracapex.cli.cli import pass_environment, Environment
from jiracapex.reporting.runner import ReportRunner

@click.command("sql", short_help="run SQL script")
@click.argument("sqlfile", type=click.Path(exists=True))
@click.option('--param',  multiple=True, type=(str, str))
@click.option('--csv', type=click.Path(dir_okay=True), required=False, default=None)
@pass_environment
def cli(ctx: Environment, sqlfile, param, csv):
    sql_params = {}
    if param is not None:
        for name, value in param:
            sql_params[name] = value

    with open(sqlfile, 'r') as reader:
        sql_query = reader.read()

    report = ReportRunner(ctx.engine())
    report.run_query(sql_query, sql_params)

    print(report.df)

    if csv is not None:
        report.df.to_csv(csv, sep=',', encoding='utf-8', index=False)


