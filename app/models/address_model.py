from argparse import ArgumentError
from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base

from .base_model import BaseModel

class AddressModel(Base, BaseModel):
    __tablename__ = "address"

    address1 = Column(String(128))
    address2 = Column(String(128))
    city = Column(String(128))
    state = Column(String(128))
    country = Column(String(64))
    user_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)

    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a diction")

        for key, value in schema.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)