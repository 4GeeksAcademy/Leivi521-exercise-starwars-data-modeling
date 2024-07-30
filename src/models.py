import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum as PyEnum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable =False)

  



class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    gender = Column(String(250), nullable=False)
    haircolor = Column(String(250), nullable=False)
    eyecolor = Column(String(250), nullable=False)
    favorite = Column(String(250), nullable=False)
    
    # character_id = Column(Integer, ForeignKey('user.id'))




class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
  
    # planet_id = Column(Integer, ForeignKey('user.id'))

    
class Starship(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable =False)
    size = Column(Integer, ForeignKey('user.id'), nullable = False)
    type = Column(String, nullable = False)
    speed = Column(Text)

    # Starship_id = Column(Integer, ForeignKey('user.id'))


class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    
    favorites_user = relationship('User')

    favorites_planets = relationship('Planet')
    favorites_characters = relationship('Character')
    favorites_starships = relationship('Starship')

 






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
