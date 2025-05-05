from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.psql import Base


class Vessel(Base):
    __tablename__ = 'vessels'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    capacity = Column(DECIMAL(10, 2))


class Port(Base):
    __tablename__ = 'ports'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255))


class Voyage(Base):
    __tablename__ = 'voyages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    vessel_id = Column(Integer, ForeignKey('vessels.id'), nullable=False)
    start_port_id = Column(Integer, ForeignKey('ports.id'), nullable=False)
    end_port_id = Column(Integer, ForeignKey('ports.id'), nullable=False)
    departure_datetime = Column(DATETIME)
    arrival_datetime = Column(DATETIME)

    vessel = relationship("Vessel")
    start_port = relationship("Port", foreign_keys=[start_port_id])
    end_port = relationship("Port", foreign_keys=[end_port_id])


class Shipment(Base):
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    voyage_id = Column(Integer, ForeignKey('voyages.id'), nullable=False)
    cargo_description = Column(String(255))
    weight = Column(DECIMAL(10, 2))
    shipped_date = Column(DATETIME)

    voyage = relationship("Voyage")


class Personnel(Base):
    __tablename__ = 'personnel'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    role = Column(String(50))


class PortCall(Base):
    __tablename__ = 'port_calls'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    voyage_id = Column(Integer, ForeignKey('voyages.id'))
    port_id = Column(Integer, ForeignKey('ports.id'))
    arrival_time = Column(DATETIME)
    departure_time = Column(DATETIME)
    responsible_personnel_id = Column(Integer, ForeignKey('personnel.id'))

    voyage = relationship("Voyage")
    port = relationship("Port")
    responsible_personnel = relationship("Personnel")
