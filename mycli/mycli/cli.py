from typing import Any

import click

from mycli.commands.users import users


@click.group()
@click.version_option()
def main() -> None:
    """My CLI tool."""
    pass


main.add_command(users)


if __name__ == "__main__":
    main()