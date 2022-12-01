#!/usr/bin/python3
"""Defines a STATE class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State (Base):
    """a class STATE instance of Base linked to "states" in MySQL table"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
