#!/usr/bin/python3
"""File that contains model city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class that presents model City"""

    __tablename__ = "cities"

    id = Column(
        Integer, nullable=False,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
