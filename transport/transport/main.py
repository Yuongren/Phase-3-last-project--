# main.py
from alembic.config import Config
from alembic import command
from src.db import DATABASE_URL

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_migrations()
