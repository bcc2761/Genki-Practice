# ORM, object relational mapping, database connection setup
# Using SQLAlchemy with SQLite for simplicity
# Allows easy database interactions using Python classes to represent tables

from sqlalchemy import Column, Integer, String, DataTime, create_engine # Core SQLAlchemy components
from sqlalchemy.ext.declarative import declarative_base # Base class for ORM models
from sqlalchemy.orm import sessionmaker # Session factory for database interactions
from datetime import datetime # For timestamp fields

engine = create_engine('sqlite:///genki_practice.db', echo=True) # SQLite database engine
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Session factory

Base = declarative_base() # Base class for ORM models

class Challenge(Base):
    __tablename__ = 'challenges' # Table name in the database

    # Challenge model columns
    id = Column(Integer, primary_key=True, index=True) # Primary key column
    user_id = Column(String, index=True) # User identifier
    challenge_type = Column(String, index=True) # Type of challenge (e.g., vocabulary, grammar)
    content = Column(String) # Content of the challenge