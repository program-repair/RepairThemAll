from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

config = dotenv_values(".env")
RDS_USERNAME = config.get('RDS_USERNAME')
RDS_PASSWORD = config.get('RDS_PASSWORD')
RDS_HOSTNAME = config.get('RDS_HOSTNAME')
RDS_DATABASE = config.get('RDS_DATABASE')
RDS_URL = 'postgresql://{}:{}@{}/{}'.format(
    RDS_USERNAME, RDS_PASSWORD, RDS_HOSTNAME, RDS_DATABASE)


def get_engine():
    return create_engine(RDS_URL)


def connect():
    connection = get_engine().connect()
    return connection


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def save(obj):
    try:
        session = get_session()
        session.add(obj)
        session.commit()
        session.close()
    except Exception as e:
        # try again!
        print('Error: {}'.format(e))
        session = get_session()
        session.add(obj)
        session.commit()
        session.close()
