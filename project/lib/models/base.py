"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))

def create_tables(engine):
    DeclarativeBase.metadata.create_all(engine)
