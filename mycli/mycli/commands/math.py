import click

from mycli.api import math


@click.command()
@click.argument("arg1", type=int)
@click.argument("arg2", type=int)
def sum(arg1: int, arg2: int) -> None:
    """Sum two integers."""
    click.echo(math.sum(arg1, arg2))
