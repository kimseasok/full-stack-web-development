from argparse import ArgumentError

from sqlalchemy import Column, Integer, String, ForeignKey, Table

from app.database import Base
from app.utits import sanitize_key

from .base_model import BaseModel


class TagModel(Base, BaseModel):
    __tablename__ = "tags"

    name = Column(String(64))
    slush = Column(String(64))
    description = Column(String(264))

    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a diction")

        for key, value in schema.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)

        self.slush = sanitize_key(schema.get("name"))
