from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Link(base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True, nullable=False)
    short_link = Column(String, nullable=False)
    visits = Column(Integer, default=0)
