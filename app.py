#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, Float

# Conexión a base de datos
 
Base = declarative_base()
engine = create_engine('sqlite:///game.db')
session_db = sessionmaker()
session_db.configure(bind=engine)

# Modelos

class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

# Rutas REST

# Main

if __name__ == '__main__':
    print('hola')
