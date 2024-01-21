
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from transport.src.models import Base, Vehicle, Route, Schedule

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.command()
def main():
    click.echo("Welcome to the Transport Project CLI!")
    create_tables()
    add_sample_data()
    display_info()

def create_tables():
    click.echo("Creating tables...")
    Base.metadata.create_all(engine)
    click.echo("Tables created successfully.")

def add_sample_data():
    click.echo("Adding sample data...")
    vehicle1 = Vehicle(name='Bus 1')
    vehicle2 = Vehicle(name='Train 1')
    route1 = Route(name='Route A')
    route2 = Route(name='Route B')
    schedule1 = Schedule(time='10:00')
    schedule2 = Schedule(time='14:00')

    route1.vehicles.append(vehicle1)
    route1.schedules.append(schedule1)
    route2.vehicles.append(vehicle2)
    route2.schedules.append(schedule2)

    session.add_all([vehicle1, vehicle2, route1, route2, schedule1, schedule2])
    session.commit()
    click.echo("Sample data added successfully.")

def display_info():
    click.echo("Displaying information...")
    vehicles = session.query(Vehicle).all()
    routes = session.query(Route).all()
    schedules = session.query(Schedule).all()

    click.echo("Vehicles:")
    for vehicle in vehicles:
        click.echo(f" - {vehicle.name}")

    click.echo("Routes:")
    for route in routes:
        click.echo(f" - {route.name}")

    click.echo("Schedules:")
    for schedule in schedules:
        click.echo(f" - Time: {schedule.time}, Route: {schedule.route.name}")

if __name__ == '__main__':
    main()
