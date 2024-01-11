# src/cli.py
import click
from src.db import SessionLocal
from src.models import Vehicle, Route, Schedule

@click.group()
def cli():
    pass

@cli.command()
def seed():
    db = SessionLocal()

    # Add seed data (you can customize this)
    vehicle1 = Vehicle(name="Bus")
    route1 = Route(name="Route A", vehicle=vehicle1)
    schedule1 = Schedule(time="8:00 AM", route=route1)

    vehicle2 = Vehicle(name="Train")
    route2 = Route(name="Route B", vehicle=vehicle2)
    schedule2 = Schedule(time="10:00 AM", route=route2)

    db.add_all([vehicle1, route1, schedule1, vehicle2, route2, schedule2])
    db.commit()
    db.close()

@cli.command()
def list_routes():
    db = SessionLocal()
    routes = db.query(Route).all()

    for route in routes:
        print(f"Route ID: {route.id}, Name: {route.name}, Vehicle: {route.vehicle.name}")

    db.close()

# You can add more CLI commands as needed

if __name__ == "__main__":
    cli()
