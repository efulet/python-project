"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from base import DeclarativeBase, db_connect


class MyTable(DeclarativeBase):
    """A simple class for access to a table"""
    __tablename__ = "my_table"
    
    id = Column(Integer, primary_key=True)
    
    def __init__(self):
        pass
    
    def length(self):
        """A simple sample how count all ids"""
        self.Session = sessionmaker(bind=db_connect())
        session = self.Session()
        counter = -1
        
        try:
            counter = session.query(self.__table__).count()
        except:
            raise
        finally:
            session.close()
        
        return counter
