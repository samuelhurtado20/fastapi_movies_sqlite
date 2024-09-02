import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "database.sqlite" # SQLite database file name

base_dir = os.path.dirname(os.path.realpath(__file__)) # Get the directory name of the current file

sqlite_file_path = os.path.join(base_dir, sqlite_file_name) # Get the full path of the database file

database_url = f"sqlite:///{sqlite_file_path}" # SQLite database URL

engine = create_engine(database_url, echo=True) # echo=True will print all SQL queries

Session = sessionmaker(bind=engine) # Create a session factory

Base = declarative_base() # Create a base class for declarative class definitions