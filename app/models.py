from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.psql import Base


class Departament(Base):
    __tablename__ = 'departaments'
    
    departament_id = Column(Integer, primary_key=True, autoincrement=True)
    departament_name = Column(String(100), nullable=False)

class Employee(Base):
    __tablename__ = 'employees'
    
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    departament_id = Column(Integer, ForeignKey('departaments.departament_id'), nullable=False)
    experience_years = Column(Integer, nullable=False)
    phone_number = Column(String(20), nullable=False)
    position = Column(String(100), nullable=False)

class Salary(Base):
    __tablename__ = 'salaries'
    
    salary_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False)
    salary_amount = Column(Integer, nullable=False)