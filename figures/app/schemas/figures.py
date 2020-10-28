"""Figures schema."""
from typing import Optional, List
from datetime import date
from pydantic import validator

from . import Model


class Figure(Model):
    name: str
    description: str
    birthdate: date
    date_death: Optional[date] = None
    tags: Optional[List[str]] = list()

    @validator('date_death')
    def date_death_must_be_bigger_than_birthdate(cls, v, values):
        if v is not None and v <= values.get('birthdate', date.max):
            raise ValueError('date_death must be bigger than birthdate')
        return v


class FigureResponse(Figure):
    id: str


class FigureUpdate(Model):
    name: Optional[str] = None
    description: Optional[str] = None
    birthdate: Optional[date] = None
    date_death: Optional[date] = None
    tags: Optional[List[str]] = None
