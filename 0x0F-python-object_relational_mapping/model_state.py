#!/usr/bin/python3
'''Modules to import'''
import sqlalchemy
from sqlalchemy import create_engine, Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    ''' class state that inherits from Base'''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
