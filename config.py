import os

class Config:

    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    DEBUG="True"
    SECRET_KEY='jklsjgkljskljgiorjiosnklfiowpnbriorbo'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://hillarydalie:password@localhost:5432/thecrucible'
    
class TestConfig():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hillarydalie:password@localhost:5432/thecrucible_test'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

configurations = { 'development':Config, 'test':TestConfig, "production":ProdConfig }