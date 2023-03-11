from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class Music(Base):
    __tablename__ = "musics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), index=True)
    singer = Column(String(256))
    level = Column(String(2), index=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
