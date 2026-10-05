from enum import Enum

import click


class Gender(Enum):
    MALE = ("male", "Male user")
    FEMALE = ("female", "Female user")
    OTHER = ("other", "Another gender")

    description: str

    def __new__(cls, value: str, description: str) -> "Gender":
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj


@click.group()
def users() -> None:
    """Manage company users."""
    pass


@users.command()
@click.option("--name", required=True, help="User's name")
@click.option("--age", type=int, required=True, help="User's age")
@click.option("--gender", type=click.Choice[Gender](Gender, case_sensitive=False), required=True, help="User's gender")
def add(name: str, age: int, gender: Gender) -> None:
    """Add a new user."""
    click.echo(f"Adding user {name}, age {age}, gender {gender.value} ({gender.description})")


if __name__ == "__main__":
    users()
