from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Comic, ComicIssue
from faker import Faker
# Create a database connection
engine = create_engine("sqlite:///data.db")

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()
faker = Faker()

# Define user data
# use faker if have time
users_data = [
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"},
    {"username": "user3", "email": "user3@example.com"},
    
    {"username": "user4", "email": "user4@example.com"},
    {"username": "user5", "email": "user5@example.com"},
    
    {"username": "user6", "email": "user12@example.com"},
    {"username": "user7", "email": "user11@example.com"},
    {"username": "user8", "email": "user10@example.com"},
]

# Create and add users to the session
users = [User(**user_data) for user_data in users_data]
session.bulk_save_objects(users)

# Commit the user data
session.commit()

# Define comic data
comics_data = [
    {
        "title": "Spiderman",
        "publisher": "Marvel",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
            {"issue_number": 3},
        ],
        "user_id": 1, 
    },                 # Assign the comic to the user with ID's
    {
        "title": "X-Men",
        "publisher": "Marvel",
        "issues": [
            {"issue_number": 100},
            {"issue_number": 101},
            {"issue_number": 102},
        ],
        "user_id": 2,  
    },
    {
        "title": "Black Panther",
        "publisher": "Marvel",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
        ],
        "user_id": 3,  
    },
    {
        "title": "Ironman",
        "publisher": "Marvel",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
        ],
    },
    {
        "title": "Justice League",
        "publisher": "DC",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
        ],
    },
    # Add Image Comics here
    {
        "title": "Spawn",
        "publisher": "Image",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
        ],
    },
    {
        "title": "The Walking Dead",
        "publisher": "Image",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
        ],
    },
    {
        "title": "Savage Dragon",
        "publisher": "Image",
        "issues": [
            {"issue_number": 1},
            {"issue_number": 2},
        ],
    },
]
# Added other publishers for comparison if time allowed
# Create and add comics with associated issues to the session
for comic_info in comics_data:
    comic = Comic(title=comic_info["title"], publisher=comic_info["publisher"])
    
    # Create ComicIssue objects and add them to the comic
    for issue_data in comic_info["issues"]:
        issue = ComicIssue(**issue_data)
        comic.issues.append(issue)
    
    # Assign the comic to a user based on the user_id
    user_id = comic_info.get("user_id")
    if user_id is not None:
        user = session.query(User).filter_by(id=user_id).first()
    if user:
            user.comics.append(comic)
    
    session.add(comic)

# Commit the comic data and relationships
session.commit()

# Close the session
#Add more relationship if time allows
session.close()
