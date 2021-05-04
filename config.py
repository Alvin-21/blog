import os

class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Alvin:monkey@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Alvin:monkey@localhost/blog'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Alvin:monkey@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}