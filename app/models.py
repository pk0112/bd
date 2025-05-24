from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.psql import Base


class Customers(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(50))
    email = Column(String(100))


class Parts(Base):
    __tablename__ = 'parts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    capacity = Column(Integer(), nullable=False)


class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    description = Column(String, nullable=False)
    fix_part_id = Column(Integer, ForeignKey('parts.id'), nullable=False)
