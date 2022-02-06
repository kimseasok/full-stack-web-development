from argparse import ArgumentError
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

from .base_model import BaseModel

class UserModel(Base, BaseModel):
    __tablename__ = "user"

    last_name = Column(String(64), nullable=False)
    first_name = Column(String(64), nullable=False)
    __email = Column("email", String(64), nullable=False)
    __password = Column("password", String(128), nullable=False)

    address = relationship("AddressModel", backref="user", lazy=True, uselist=False)

    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a diction")

        for key, value in schema.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)

    @property
    def email(self):
        # condiction
        # security check 1
        # security check 2
        return self.__email

    @email.setter
    def email(self, email):
        # condiction
        # security check 1
        # security check 2
        self.__email = email


    def set_password(self, password):
        # condiction
        # security check 1
        # hash password before save
        self.__password = password
        