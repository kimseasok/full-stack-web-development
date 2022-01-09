from sqlalchemy import Column, Integer, String

from ..database import Base

class ForumModel(Base):

    __tablename__ = "forum"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64))
    descrciption = Column(String(250))

    def __init__(self, title, description) -> None:
        self.title = title
        self.descrciption = description