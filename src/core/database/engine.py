from sqlalchemy import create_engine
from sqlalchemy.engine import URL


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
