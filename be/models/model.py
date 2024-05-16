from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Video(Base):
    __tablename__ = 'videos'
    id = Column(String(255), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    url = Column(String(255), nullable=False)
    formats = relationship('Format', back_populates='video')

class Format(Base):
    __tablename__ = 'formats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=False)
    url = Column(String(500), nullable=False)
    size = Column(String(255), nullable=True)
    video_id = Column(String(255), ForeignKey('videos.id'))
    video = relationship('Video', back_populates='formats')

# Example configuration for SQLite (change as needed)