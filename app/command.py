"""
This module contains the command-line interface (CLI) for the application.
"""

import typer
import pyfiglet

from app.etl import ETL

cli = typer.Typer(add_completion=False)


@cli.callback()
def main():
    print(pyfiglet.figlet_format("POSTER KATA", width=1000, font='small'))


@cli.command()
def load_source_data():
    """
    Loads the source data into the database.
    """
    loader = ETL()
    loader.load_source_data()

@cli.command()
def transform_load_dw_data():
    """
    Transforms and loads the data into the data warehouse.
    """
    loader = ETL()
    loader.transform_load_dw_data()

if __name__ == '__main__':
    cli()
