#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from base import ModelBase

class User(ModelBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
       return "<User(id='%d', email='%s', first_name='%s', last_name='%s')>" % (
                            self.id, self.email, self.first_name, self.last_name)
