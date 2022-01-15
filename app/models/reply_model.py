from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base

class ReplyModel(Base):

    __tablename__ = "reply"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    content = Column(String(250))
    parent_id = Column(Integer, default=0, nullable=True)
    forum_id = Column(Integer, ForeignKey("forum.id"), nullable=False)

    def __init__(self, title, content, forum_id, parent_id=0) -> None:
        self.title = title
        self.content = content
        self.forum_id = forum_id
        self.parent_id = parent_id