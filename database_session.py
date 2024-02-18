import sqlalchemy as sa

from contextlib import contextmanager
from database import Base
from sqlalchemy.orm import sessionmaker

main_engine = sa.create_engine('postgres://loclahost:', echo=True)

database_session = sessionmaker(binds={Base: main_engine}, expire_on_commit=False)


@contextmanager
def session_scope():
    session = database_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
