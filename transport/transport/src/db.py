# src/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///./transport.db"

# Create an engine using the database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
