from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class ForumModel(Base):

    __tablename__ = "forum"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64))
    descrciption = Column(String(250))

    replies = relationship("ReplyModel", backref="forum", lazy=True)

    def __init__(self, title, description) -> None:
        self.title = title
        self.descrciption = description