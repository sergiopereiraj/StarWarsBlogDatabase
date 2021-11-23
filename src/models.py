import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Perfiles(Base):
    __tablename__ = 'perfiles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ciudad = Column(String(250))
    edad = Column(Integer)
    descripcion = Column(String(250))

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, nullable=False)
    user_name = Column(String, nullable=False)
    password = Column(String(250), nullable=False)
    perfiles = relationship(Perfiles)

class Personajes(Base):
    __tablename__ = 'personajes'
    user_id = Column(Integer, ForeignKey("users.user_id"))
    ejercito_al_que_pertenece = Column(String(250))
    edad = Column(Integer)
    civilizacion_planeta = Column(String(250))
    users = relationship(Users)

class Personajes(Base):
    __tablename__ = 'personajes'
    user_id = Column(Integer, ForeignKey("users.user_id"))
    ejercito_al_que_pertenece = Column(String(250))
    edad = Column(Integer)
    civilizacion_planeta = Column(String(250))
    users = relationship(Users)

class Naves(Base):
    __tablename__ = 'naves'
    user_id = Column(Integer, ForeignKey("users.user_id"))
    forma_de_desplazar = Column(String(250))
    color = Column(String(250))
    piloto = Column(String(250))
    users = relationship(Users)

class Armas(Base):
    __tablename__ = 'armas'
    user_id = Column(Integer, ForeignKey("users.user_id"))
    daño_arma = Column(String(250))
    tamaño_arma = Column(String(250))
    users = relationship(Users)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')