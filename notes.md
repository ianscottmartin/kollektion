# Catalogue comic books by publisher and user

#CLI is a command line interface program

# 1. create virtual environment- had to delete pipfile and pipfile.lock in main directory

# 2. install dependencies

# a. SQLAlchemy 1.4.41

    # b. Alembic (migration manager)

    # c. ipdb as a debugger

    # d. faker-generate fake data

# 4. create the migration environment

# 5. alembic init migrations

    start with initial alembic migration

# 6. configure the migration environment (alembic.ini and env.py) finished

pipenv install && pipenv shell

# 7. create declarative environment

# 8 create schema python classes or models(flush put all ideas)

# 9. populate the database with seeds

check seeds with sqlaexplorer

# 10. test the environment relationships one to many(work on many to many as well)

# 11 Deliverables

Aggregate methods to project
-CRUD
-Create- create list(join table)
-Read
-display all comics
-display liked comics

    -Update-
    -Delete remove from list of liked
