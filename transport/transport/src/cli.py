
import click
from src.db import SessionLocal
from src.models import Vehicle, Route, Schedule

# Initialize Click command group
@click.group()
def cli():
    pass

# Seed data into the database
@cli.command()
def seed():
    db = SessionLocal()

    # Add seed data 
    vehicle1 = Vehicle(name="Bus")
    route1 = Route(name="Route A", vehicle=vehicle1)
    schedule1 = Schedule(time="8:00 AM", route=route1)

    vehicle2 = Vehicle(name="Train")
    route2 = Route(name="Route B", vehicle=vehicle2)
    schedule2 = Schedule(time="10:00 AM", route=route2)

    db.add_all([vehicle1, route1, schedule1, vehicle2, route2, schedule2])
    db.commit()
    db.close()

# List all routes
@cli.command()
def list_routes():
    db = SessionLocal()
    routes = db.query(Route).all()

    for route in routes:
        print(f"Route ID: {route.id}, Name: {route.name}, Vehicle: {route.vehicle.name}")

    db.close()

# Print each route

if __name__ == "__main__":
    cli()
