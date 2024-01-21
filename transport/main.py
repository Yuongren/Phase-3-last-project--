
from alembic.config import Config
from alembic import command
from src.db import DATABASE_URL

# Function to run database migrations
def run_migrations():
    alembic_cfg = Config("alembic.ini")

    # Run the upgrade command to apply any pending migrations
    command.upgrade(alembic_cfg, "head")

# Check if the script is being run directly
if __name__ == "__main__":
     # Call the run_migrations function to apply any pending migrations
    run_migrations()
