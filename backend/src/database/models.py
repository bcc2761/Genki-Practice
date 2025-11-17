# ORM, object relational mapping, database connection setup
# Using SQLAlchemy with SQLite for simplicity
# Allows easy database interactions using Python classes to represent tables

from sqlalchemy import Column, Integer, String, DateTime, create_engine # Core SQLAlchemy components
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
    chapter = Column(Integer, index=True) # Chapter number
    date_created = Column(DateTime, default=datetime.now) # Timestamp of creation
    created_by = Column(String, nullable=False) # Creator identifier
    title = Column(String, nullable=False) # Title of the challenge
    options = Column(String, nullable=False) # Possible options for the challenge
    correct_answer_id = Column(Integer, nullable=False) # ID of the correct answer
    explanation = Column(String, nullable=False) # Explanation for the answer
    # user_id = Column(String, index=True) # User identifier
    # challenge_type = Column(String, index=True) # Type of challenge (e.g., vocabulary, grammar)
    # content = Column(String) # Content of the challenge

class ChallengeQuota(Base):
    __tablename__ = 'challenge_quotas' # Table name in the database

    # ChallengeQuota model columns
    id = Column(Integer, primary_key=True, index=True) # Primary key column
    user_id = Column(String, nullable=False, unique=True) # User identifier
    quota_remaining = Column(Integer, nullable=False, default=20)
    # chapter = Column(Integer, index=True) # Chapter number
    # quota = Column(Integer, default=0) # Number of challenges created by the user for the chapter
    last_reset_date = Column(DateTime, default=datetime.now) # Timestamp of last quota reset

Base.metadata.create_all(bind=engine) # Create tables in the database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Session factory

def get_db():
    # From documentation
    db = SessionLocal()
    try:
        yield db # yield is a generator, allows function to return a value and later resume
    finally:
        db.close()