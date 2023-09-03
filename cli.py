#!/usr/bin/env python

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User  # Import your SQLAlchemy User model

# Define the database connection
DATABASE_URL = "sqlite:///data.db"

# Initialize the users variable as an empty list
users = []

# Create a Click Group
@click.group()
def cli():
    pass

# Define the add-user command
@cli.command()
@click.argument("username")
@click.argument("email")
def add_user(username, email):
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

    # Query all users from the User table and store them in the users variable
    global users
    users = session.query(User).all()

if not users:
        print("No users found.")
else:
        print("List of users:")
        for user in users:
            print(f"Username: {user.username}, Email: {user.email}")

# Run the CLI
if __name__ == "__main__":
    cli()
