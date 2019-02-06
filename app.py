#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, Float
from bottle import Bottle, run, HTTPResponse, static_file, redirect, error, template

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

app = bottle.app()

@app.route('/')
def index():
    return 'hola desde el servidor'

# Main

if __name__ == '__main__':
    bottle.run(app = app, host='localhost', port=4000, debug=True, reloader=True)
