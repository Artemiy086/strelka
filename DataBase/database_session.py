import os

import click
import sqlalchemy as sa

from contextlib import contextmanager
from sqlalchemy.orm import Session
from flask import g
#  flask --app flaskp init-db


def get_engine():
    """Returns the database connection object"""
    engine = getattr(g, "_engine", None)

    if engine is None:
        engine = sa.create_engine(f"postgresql+psycopg2://"
                                  f"{os.environ.get('PG_ADMIN_USERNAME')}:{os.environ.get('PG_ADMIN_PSW')}"
                                  f"@127.0.0.1:5432/strelka")
    return engine


def close_engine(e=None):
    """Close all sessions"""
    database_session = g.pop("_database_session", None)

    if database_session is not None:
        database_session.close_all()


def init_db():
    from DataBase.scheme import Base

    engine = get_engine()
    Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    engine = get_engine()
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_engine)
    app.cli.add_command(init_db_command)
