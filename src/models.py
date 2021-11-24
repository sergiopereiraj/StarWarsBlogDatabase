import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    personajes = relationship("Personajes")
    naves = relationship("Naves")
    armas = relationship("Armas")

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    ejercito_al_que_pertenece = Column(String(250))
    edad = Column(Integer)
    civilizacion_planeta = Column(String(250))
    user_id = Column(Integer, ForeignKey("users.id"))

class Nave(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    forma_de_desplazar = Column(String(250))
    color = Column(String(250))
    piloto = Column(String(250))
    user_id = Column(Integer, ForeignKey("users.id"))  

class Arma(Base):
    __tablename__ = 'armas'
    id = Column(Integer, primary_key=True)
    daño_arma = Column(String(250))
    tamaño_arma = Column(String(250))
    user_id = Column(Integer, ForeignKey("users.id"))   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')