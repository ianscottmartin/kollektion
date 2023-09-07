import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Comic

# ASCII banner from https://patorjk.com/software/taag/#p=display&f=Ogre&t=Comic%20Collector
BANNER = """
   ___                _          ___      _ _           _             
  / __\___  _ __ ___ (_) ___    / __\___ | | | ___  ___| |_ ___  _ __ 
 / /  / _ \| '_ ` _ \| |/ __|  / /  / _ \| | |/ _ \/ __| __/ _ \| '__|
/ /__| (_) | | | | | | | (__  / /__| (_) | | |  __/ (__| || (_) | |   
\____/\___/|_| |_| |_|_|\___| \____/\___/|_|_|\___|\___|\__\___/|_|   
                                                                      
"""
# Define the database connection
DATABASE_URL = "sqlite:///data.db"


# Initialize SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


# Function to display the welcome menu
def welcome_menu():
    click.clear()  # Clear the console
    click.echo(BANNER)
    click.echo("Welcome to Comic Collector!")

    click.echo("1. User Management")
    click.echo("2. Comic Management")
    click.echo("3. Quit")


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
            list_users()
        elif choice == "2":
            add_user()
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

    # Query the User table and fetch all users
    users = session.query(User).all()

    if not users:
        click.echo("No users found.")
    else:
        click.echo("List of users:")
        for user in users:
            click.echo(f"Username: {user.username}, Email: {user.email}")

    press_enter_to_continue(user_management_menu)


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

    press_enter_to_continue(comic_management_menu)


# Function to display a message and wait for user input to continue
def press_enter_to_continue(next_menu_func=None):
    input("Press Enter to continue...")
    if next_menu_func:
        next_menu_func()  # Call the specified menu function


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
    press_enter_to_continue(user_management_menu)


# Define the add-comic command
@cli.command()
def add_comic():
    # Get user inputs for comic title and publisher
    title = input("Enter comic title: ")
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
    press_enter_to_continue(comic_management_menu)


# Run the CLI
if __name__ == "__main__":
    while True:
        welcome_menu()

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            user_management_menu()
        elif choice == "2":
            comic_management_menu()
        elif choice == "3":
            break
