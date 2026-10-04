from enum import Enum
import click


class Gender(str, Enum):
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
@click.option("--gender", type=click.Choice([e.value for e in Gender]), required=True, help="User's gender")
def add(name, age, gender):
    """Add a new user."""
    click.echo(f"Adding user {name}, age {age}, gender {gender}")


if __name__ == "__main__":
    users()
