from . import app
from server.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import datetime

# Base = declarative_base()

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.BigInteger, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def save(self):
        self.updated_on = datetime.datetime.utcnow()
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
    
    def __repr__(self): # return format when queried
        return '<%s %d>' % (self.__class__.__name__, self.id)    

class User(Base):
    __tablename__ = 'users'
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    photo = db.Column(db.Text)

    @staticmethod
    def query_by_user_id(user_id):
        if user_id is None:
            return None
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def query_by_email(email):
        if email is None:
            return None
        return User.query.filter_by(email=email).first()