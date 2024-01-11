# src/models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    routes = relationship('Route', back_populates='vehicle')

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship('Vehicle', back_populates='routes')
    schedule = relationship('Schedule', back_populates='route')

class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True)
    time = Column(String, nullable=False)
    route_id = Column(Integer, ForeignKey('routes.id'))
    route = relationship('Route', back_populates='schedule')

# You can add more columns as per your requirement
