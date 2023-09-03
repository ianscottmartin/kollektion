#!/usr/bin/env python
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Comic  # Import SQLAlchemy User and Comic models

# Define the database connection
DATABASE_URL = "sqlite:///data.db"

# ASCII banner from https://patorjk.com/software/taag/#p=display&f=Ogre&t=Comic%20Collector
BANNER = """
   ___                _          ___      _ _           _             
  / __\___  _ __ ___ (_) ___    / __\___ | | | ___  ___| |_ ___  _ __ 
 / /  / _ \| '_ ` _ \| |/ __|  / /  / _ \| | |/ _ \/ __| __/ _ \| '__|
/ /__| (_) | | | | | | | (__  / /__| (_) | | |  __/ (__| || (_) | |   
\____/\___/|_| |_| |_|_|\___| \____/\___/|_|_|\___|\___|\__\___/|_|   
                                                                      
"""

# Function to display the welcome menu
def welcome_menu():
    click.clear()  # Clear the console
    click.echo(BANNER)
    click.echo("Welcome to Comic Collector!")
    click.echo("1. User Management")
    click.echo("2. Comic Management")
    click.echo("3. Quit")

    choice = input("Enter your choice (1/2/3): ")
    return choice

# Function to display the user menu
def user_management_menu():
    while True:
        click.clear()  # Clear the console
        click.echo("User Management Menu:")
        click.echo("1. List Users")
        click.echo("2. Add User")
        click.echo("3. Back to Main Menu")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            list_users()  # Call the list_users function

        elif choice == "2":
            add_user()  # Call the add_user function

        elif choice == "3":
            break

# Function to display the comic menu
def comic_management_menu():
    while True:
        click.clear()  # Clear the console
        click.echo("Comic Management Menu:")
        click.echo("1. List Comics")
        click.echo("2. Add Comic")
        click.echo("3. Back to Main Menu")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            list_comics()  # Call the list_comics function

        elif choice == "2":
            add_comic()  # Call the add_comic function

        elif choice == "3":
            break

# Function to display a message and wait for user input to continue
def press_enter_to_continue(message="Press Enter to continue..."):
    input(message)

# Function to list users
def list_users():
    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the User table and fetch all users
    users = session.query(User).all()

    if not users:
        click.echo("No users found.")
    else:
        click.echo("List of users:")
        for user in users:
            click.echo(f"Username: {user.username}, Email: {user.email}")
        press_enter_to_continue("Press Enter to go back...")

# Function to list comics
def list_comics():
    # Initialize SQLAlchemy engine and session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the Comic table and fetch all comics
    comics = session.query(Comic).all()

    if not comics:
        click.echo("No comics found.")
    else:
        click.echo("List of comics:")
        for comic in comics:
            click.echo(f"Title: {comic.title}, Publisher: {comic.publisher}")
        press_enter_to_continue("Press Enter to go back...")

# Main CLI function
@click.group()
def cli():
    pass

# Define the add-user command
@cli.command()
def add_user():
    while True:
        # Get user inputs for username and email
        username = input("Enter username (or 'B' to go back): ")
        
        if username.strip().lower() == 'b':
            break
        
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

        # Add a back option
        back_option = input("Enter 'b' to go back to the previous menu or press Enter to continue: ").strip().lower()
        if back_option == "b":
            break

# Define the add-comic command
@cli.command()
def add_comic():
    while True:
        # Get user inputs for comic title and publisher
        title = input("Enter comic title (or 'b' to go back): ")
        
        if title.strip().lower() == 'b':
            break
        
        publisher = input("Enter comic publisher: ") 

        # Initialize SQLAlchemy session
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create a new Comic object and add it to the database
        comic = Comic(title=title, publisher=publisher)  
        session.add(comic)
        session.commit()

        print(f"Comic '{title}' by {publisher} added successfully.")

        # Add a back option
        back_option = input("Enter 'B' to go back to the previous menu or press Enter to continue: ").strip().lower()
        if back_option == "b":
            break

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

