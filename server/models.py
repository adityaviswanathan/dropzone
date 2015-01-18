from . import app
from server.db import db
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_Distance
import datetime
import math

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
    drops = relationship('Drop', backref='users')
    pickups = relationship('Pickup', backref='users')

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

    # returns list
    @staticmethod
    def get_nearby_drops(lat, lng):
        drops = Drop.query.all()
        nearby_drops = []
        for drop in drops:
            dlat = lat - drop.lat
            dlng = lng - drop.lng
            distance = math.sqrt(dlat * dlat + dlng * dlng)
            # distance = db.engine.execute("SELECT ST_Distance(ST_GeomFromText('POINT({0} {1})'), ST_GeomFromText('POINT({2} {3})'));".format(lat, lng, drop.lat, drop.lng)).first()
            print distance
            if distance < 1.0:
                print "yay"
                nearby_drops.append(drop)
        return nearby_drops


class Drop(Base):
    __tablename__ = 'drops'
    data_type = db.Column(db.Enum('text','photo','video', name='data_types'))
    data_payload = db.Column(db.Text)
    numviews = db.Column(db.Integer)
    restrictions = db.Column(db.Enum('self', 'friends', 'public', name='restriction_types'))
    viewcap = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    teaser = db.Column(db.Text)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    # def set_location(self, lat, lng):
    #     result = db.engine.execute("SELECT ST_AsText(ST_MakePoint({0}, {1}));".format(lat, lng))
    #     self.location = result.first()[0]

    @staticmethod
    def query_by_drop_id(drop_id):
        if drop_id is None:
            return None
        return Drop.query.filter_by(id=drop_id).first()

class Pickup(Base):
    __tablename__ = 'pickups'
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    drop_id = db.Column(db.Integer, ForeignKey('drops.id'))

    @staticmethod
    def query_by_pickup_id(pickup_id):
        if pickup_id is None:
            return None
        return Pickup.query.filter_by(id=pickup_id).first()

    # returns list
    @staticmethod
    def query_by_drop_id(drop_id):
        if drop_id is None:
            return None
        return Pickup.query.filter_by(drop_id=drop_id)

    # returns list
    @staticmethod
    def query_by_user_id(user_id):
        if user_id is None:
            return None
        return Pickup.query.filter_by(user_id=user_id)
