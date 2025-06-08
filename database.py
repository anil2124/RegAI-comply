# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This URL now points to the PostgreSQL database running inside our Docker container.
# Format: postgresql://[USER]:[PASSWORD]@[HOST]/[DB_NAME]
# - HOST is 'localhost' because we mapped the container's port 5432 to our machine's port 5432.
SQLALCHEMY_DATABASE_URL = "postgresql://regai_user:regai_password@localhost/regai_db"

# The engine is the main entry point for SQLAlchemy to talk to the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# A SessionLocal class acts as a factory for creating new database sessions.
# A session is like a temporary conversation with the database for a single
# set of operations.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We create a 'Base' class here. Our SQLAlchemy model classes (like the one
# in models.py) will inherit from this Base. This is how SQLAlchemy's ORM
# discovers our table models.
Base = declarative_base()
