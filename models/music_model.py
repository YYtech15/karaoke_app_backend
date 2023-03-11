from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class Music(Base):
    __tablename__ = "musics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), index=True)
    singer = Column(String(256), index=True)
    level = Column(String(2), index=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    url = relationship("Url", back_populates="music")

class Url(Base):
    __tablename__ = "Urls"

    id = Column(Integer, ForeignKey("musics.id"), primary_key=True)
    url = Column(String(256), index=True)

    music = relationship("Music", back_populates="url")