from argparse import ArgumentError

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

from .base_model import BaseModel


class ForumModel(Base, BaseModel):

    __tablename__ = "forum"

    title = Column(String(64))
    description = Column(String(250))
    slush = Column(String(128))

    replies = relationship("ReplyModel", backref="forum", lazy=True)

    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a diction")

        for key, value in schema.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)
