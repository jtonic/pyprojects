from typing import Any

import click

from mycli.commands.math import sum
from mycli.commands.users import users


@click.group()
@click.version_option()
def main() -> None:
    """My CLI tool."""
    pass


main.add_command(users)
main.add_command(sum)


if __name__ == "__main__":
    main()
