from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.psql import Base


class Teams(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    league = Column(String, nullable=False)


class Players(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    team_id = Column(Integer(), ForeignKey('teams.id'), nullable=False)


class Matches(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    team_1 = Column(Integer(), ForeignKey('teams.id'), nullable=False)
    team_2 = Column(Integer(), ForeignKey('teams.id'), nullable=False)
    league = Column(String)


class Goals(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(Integer, ForeignKey('matches.id'), nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)