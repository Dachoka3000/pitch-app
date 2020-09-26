import os

class Config:
    '''
    contains general configuration code
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    subclass of Config with configurations for production mode
    '''
    pass

class DevConfig(Config):
    '''
    subclass of config class with configurations for development mode
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}