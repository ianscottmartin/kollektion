#!/usr/bin/env python
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User  # Import your SQLAlchemy User model

# Define the database connection
DATABASE_URL = "sqlite:///data.db"

# Create a Click Group
@click.group()
def cli():
    pass

# Define the add-user command
@cli.command()
def add_user():
    # Prompt the user for username and email
    username = click.prompt("Enter username")
    email = click.prompt("Enter email")

    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new User object and add it to the database
    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    print(f"User {username} with email {email} added successfully.")

# Define the list-users command
@cli.command()
def list_users():
    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    global users  # Move this line here to ensure variable scope

    while True:
        click.clear()  # Clear the console
        click.echo("User Management Menu:")
        click.echo("1. List Users")
        click.echo("2. Add User")
        click.echo("3. Quit")

        choice = click.prompt("Enter your choice (1/2/3)", type=int)

        if choice == 1:
            users = session.query(User).all()

            if not users:
                click.echo("No users found.")
            else:
                click.echo("List of users:")
                for user in users:
                    click.echo(f"Username: {user.username}, Email: {user.email}")
            click.pause()

        elif choice == 2:
            # Prompt the user for username and email
            username = click.prompt("Enter username")
            email = click.prompt("Enter email")

            # Create a new User object and add it to the database
            user = User(username=username, email=email)
            session.add(user)
            session.commit()

            click.echo(f"User {username} with email {email} added successfully.")
            click.pause()

        elif choice == 3:
            break

# Run the CLI
if __name__ == "__main__":
    cli()
