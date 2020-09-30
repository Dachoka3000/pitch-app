import os

class Config:
    '''
    contains general configuration code
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    '''
    subclass of Config with configurations for production mode
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    subclass of config class with configurations for development mode
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daisy:4H@ppyfeet@localhost/pitchup'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}