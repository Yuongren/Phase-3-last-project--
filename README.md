# Phase-3-last-project--

## Transport Management system

This systems helps to solve the problem of managing a transport system, providing a structured way to store and retrieve information about users, vehicles, and trips.
This project defines the data schema and CLI interface for managing transport scheduling data in a SQLite database.

## Project Structure

transport/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── db.py
│   └── cli.py
│
└── main.py

## Models

The data schema is defined in models.py. It consists of 3 database tables:

Vehicles - Stores vehicle details like name
Routes - Stores route details and links to a vehicle
Schedules - Stores schedules for routes including time
Relationships are defined between the tables using SQLAlchemy.

## CLI

A CLI is provided in cli.py using the Click library. It currently supports:

seed - Populates the database with sample data
list-routes - Lists all routes with associated vehicle name
Additional commands can be added as needed.

## Database

The database connection and sessionmaker are defined in db.py. It uses SQLAlchemy to connect to a SQLite database file at transport.db.

## Migrations

Database schema migrations are supported using Alembic. main.py runs the initial migration to apply the schema on startup. The migration configuration is defined in alembic.ini.

## Project Setup

First clone the repository: git clone [https://github.com/Yuongren/Phase-3-last-project--/tree/main]. Then open the cloned repository: cd -- cloned repository -- .Then create virtual environment by running pipenv install and then shell.By running pipenv install you install the required dependuncies.

## Author

Youngren Gitonga.
For any questions or issues, please contact [Your Name] at [youngrengitonga@gmail.com].

## linces

This project has been released under the MIT Linces, to see more read license file.