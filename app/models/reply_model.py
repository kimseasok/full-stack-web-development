from argparse import ArgumentError

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.database import Base

from .base_model import BaseModel

association_table = Table(
    "forum_tag",
    Base.metadata,
    Column("reply_id", ForeignKey("reply.id")),
    Column("tag_id", ForeignKey("tags.id")),
)


class ReplyModel(Base, BaseModel):

    __tablename__ = "reply"

    title = Column(String(64), nullable=False)
    content = Column(String(250))
    parent_id = Column(Integer, default=0, nullable=True)

    forum_id = Column(Integer, ForeignKey("forum.id"), nullable=False)

    tags = relationship(
        "TagModel", secondary=association_table, backref="replies", lazy=True
    )

    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a diction")

        for key, value in schema.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)
