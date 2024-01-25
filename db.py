# Import SQLAlchemy functions and classes
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL (PostgreSQL in this case)
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/phoneproject"

# Create a SQLAlchemy engine to manage database connections
engine = create_engine(DATABASE_URL)

# Create a sessionmaker object for creating new database sessions
# - autocommit=False: Sessions will not automatically commit changes to the database
# - autoflush=False: Objects loaded within the session will not be automatically refreshed 
#                    to reflect changes made in the database
# - bind=engine: Associate the sessionmaker with the database engine created above
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
# This will be used as a base class by all ORM classes in the application
Base = declarative_base()

# Note: The above code sets up the database connection and session management 
#       using SQLAlchemy. This configuration allows you to define ORM classes 
#       (models) and perform CRUD operations using these models to interact 
#       with the PostgreSQL database specified in the DATABASE_URL.
