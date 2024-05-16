import json
import os
import zipfile

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models.model import Video, Format, Base


class Engine:
    def __init__(self, database_uri):
        self.database_uri = database_uri
        self.engine = create_engine(database_uri)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_engine(self):
        return self.engine


class Repository:
    def __init__(self):
        DATABASE_URI = 'mysql://root:@localhost:3306/youtube-loader'
        engine = Engine(DATABASE_URI)
        # Create tables
        Base.metadata.create_all(engine.get_engine())
        self.engine = engine


class VideoRepository(Repository):
    def add_video(self, id, name, url):
        session = self.engine.get_session()
        video = Video(id=id, name=name, url=url)
        session.add(video)
        session.commit()
        session.close()

    def get_video_by_id(self, video_id):
        session = self.engine.get_session()
        video = session.query(Video).filter_by(id=video_id).options(joinedload(Video.formats)).first()
        session.close()
        return video

    def get_count(self):
        session = self.engine.get_session()
        count = session.query(Video).count()
        return count

    # Thêm các phương thức khác cần thiết tại đây


class FormatRepository(Repository):
    def add_format(self, type, url, video_id, size):
        session = self.engine.get_session()
        format = Format(type=type, url=url, video_id=video_id, size=size)
        session.add(format)
        session.commit()
        session.close()

    def get_formats_by_video_id(self, video_id):
        session = self.engine.get_session()
        formats = session.query(Format).filter_by(video_id=video_id).all()
        session.close()
        return formats


# Thêm các phương thức khác cần thiết tại đây

