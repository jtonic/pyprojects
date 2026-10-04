from enum import Enum

import click


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


@click.group()
def users():
    """Manage company users."""
    pass


@users.command()
@click.option("--name", required=True, help="User's name")
@click.option("--age", type=int, required=True, help="User's age")
@click.option("--gender", type=click.Choice(Gender, case_sensitive=False), required=True, help="User's gender")
def add(name: str, age: int, gender: Gender) -> None:
    """Add a new user."""
    click.echo(f"Adding user {name}, age {age}, gender {gender.value}")


if __name__ == "__main__":
    users()
