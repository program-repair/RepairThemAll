from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


def get_engine():
    url = URL.create(
        drivername="postgresql",
        username="postgres",
        password="root",
        database="plm"
    )
    return create_engine(url)


def connect():
    connection = get_engine().connect()
    return connection


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def save(obj):
    session = get_session()
    session.add(obj)
    session.commit()
    session.close()
