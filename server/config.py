import os
from server.login import facebook, facebook_dev

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '\\\xb3\x94?\xb0\xf2:f|\xab\xbaK\xfe%0|gY\x9e\x10D\x91\tl'
    SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://aklcjsnfxbvrbf:cNoCSeGAX-SvtQUddKYCAkzk11@ec2-50-16-190-77.compute-1.amazonaws.com:5432/dll4ul1cuc1kh'
    FACEBOOK_AUTH = facebook

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dropzone'
    SERVER_NAME = 'localhost:5000'
    PREFERRED_URL_SCHEME = 'http'
    FACEBOOK_AUTH = facebook_dev

class TestingConfig(Config):
    TESTING = True