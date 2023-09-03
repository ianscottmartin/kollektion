import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Comic  # Import your SQLAlchemy models
