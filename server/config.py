import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '\\\xb3\x94?\xb0\xf2:f|\xab\xbaK\xfe%0|gY\x9e\x10D\x91\tl'
    SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://ucfkdd2nnohmef:p5f86vp1pohq1mbj1of6rh0u3q1@ec2-54-235-171-105.compute-1.amazonaws.com:5702/d3e21gohnca0fi'

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dropzone'
    SERVER_NAME = 'localhost:5000'
    PREFERRED_URL_SCHEME = 'http'

class TestingConfig(Config):
    TESTING = True