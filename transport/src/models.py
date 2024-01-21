
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Define the base class for all models
Base = declarative_base()

# Define the Vehicle model
class Vehicle(Base):
    # Define the name of the table in the database
    __tablename__ = 'vehicles'

    # Define the columns of the table
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Define the relationship between Vehicle and Route
    routes = relationship('Route', back_populates='vehicle')

# Define the Route model
class Route(Base):
    # Define the name of the table in the database
    __tablename__ = 'routes'
    # Define the columns of the table
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    # Define the relationship between Route and Vehicle
    vehicle = relationship('Vehicle', back_populates='routes')
    # Define the relationship between Route and Schedule
    schedule = relationship('Schedule', back_populates='route')

# Define the Schedule model
class Schedule(Base):
    # Define the name of the table in the database
    __tablename__ = 'schedules'
    # Define the columns of the table
    id = Column(Integer, primary_key=True)
    time = Column(String, nullable=False)
    route_id = Column(Integer, ForeignKey('routes.id'))
    route = relationship('Route', back_populates='schedule')

