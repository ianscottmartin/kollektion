from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(55), unique=True)
    email = Column(String(100), unique=True)  # Adjust the length as needed, not that need so many characters

    # Define a one-to-many relationship between User and Comic
    comics = relationship("Comic", back_populates="user")

    # Define unique constraints, out of time
    # Example: UniqueConstraint('username', 'email', name='unique_username_email')
    #Didn't work for me, too many errors, missing something

class Comic(Base):    #Create Comic table
    __tablename__ = "comic"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher = Column(String)

    # Define a many-to-one relationship between Comic and User
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="comics") #back_ref not functioning

    # Create a one-to-many relationship with ComicIssue
    issues = relationship("ComicIssue", back_populates="comic")

class ComicIssue(Base):
    __tablename__ = "comic_issue"

    id = Column(Integer, primary_key=True)
    issue_number = Column(Integer)
    comic_id = Column(Integer, ForeignKey("comic.id"))


    # Establish a back-reference to the Comic table/ used instead of back_ref
    comic = relationship("Comic", back_populates="issues")
