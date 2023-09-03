#!/usr/bin/env python
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Comic  # Import your SQLAlchemy User and Comic models

# Define the database connection
DATABASE_URL = "sqlite:///data.db"

# ASCII banner
BANNER = """
  ____ _ _       ____                      _       
 / ___(_) |_    / ___|___  _ __ ___  _ __ (_) __ _ 
| |   | | __|  | |   / _ \| '_ ` _ \| '_ \| |/ _` |
| |___| | |_   | |__| (_) | | | | | | |_) | | (_| |
 \____|_|\__|   \____\___/|_| |_| |_| .__/|_|\__,_|
                                   |_|            
"""

# Function to display the welcome menu
def welcome_menu():
    click.clear()  # Clear the console
    click.echo(BANNER)
    click.echo("Welcome to Your CLI Application!")
    click.echo("1. User Management")
    click.echo("2. Comic Management")
    click.echo("3. Quit")

    choice = input("Enter your choice (1/2/3): ")
    return choice

# Function to display the user management menu
def user_management_menu():
    while True:
        click.clear()  # Clear the console
        click.echo("User Management Menu:")
        click.echo("1. List Users")
        click.echo("2. Add User")
        click.echo("3. Back to Main Menu")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            list_users()
        elif choice == "2":
            add_user()
        elif choice == "3":
            break

# Function to display the comic management menu
def comic_management_menu():
    while True:
        click.clear()  # Clear the console
        click.echo("Comic Management Menu:")
        click.echo("1. List Comics")
        click.echo("2. Add Comic")
        click.echo("3. Back to Main Menu")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            list_comics()
        elif choice == "2":
            add_comic()
        elif choice == "3":
            break

# Function to list users
def list_users():
    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(User).all()

    if not users:
        click.echo("No users found.")
    else:
        click.echo("List of users:")
        for user in users:
            click.echo(f"Username: {user.username}, Email: {user.email}")

# Function to list comics
def list_comics():
    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    comics = session.query(Comic).all()

    if not comics:
        click.echo("No comics found.")
    else:
        click.echo("List of comics:")
        for comic in comics:
            click.echo(f"Title: {comic.title}, Publisher: {comic.publisher}")

# Main CLI function
@click.group()
def cli():
    pass

# Define the add-user command
@cli.command()
def add_user():
    # Get user inputs for username and email
    username = input("Enter username: ")
    email = input("Enter email: ")

    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new User object and add it to the database
    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    print(f"User {username} with email {email} added successfully.")

# Define the add-comic command (with 'Publisher' instead of 'Author')
@cli.command()
def add_comic():
    # Get user inputs for comic title and publisher
    title = input("Enter comic title: ")
    publisher = input("Enter comic publisher: ")  # Changed 'author' to 'publisher'

    # Initialize SQLAlchemy session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new Comic object and add it to the database
    comic = Comic(title=title, publisher=publisher)  # Changed 'author' to 'publisher'
    session.add(comic)
    session.commit()

    print(f"Comic '{title}' by {publisher} added successfully.")

# Run the CLI
if __name__ == "__main__":
    while True:
        choice = welcome_menu()

        if choice == "1":
            user_management_menu()
        elif choice == "2":
            comic_management_menu()
        elif choice == "3":
            break

