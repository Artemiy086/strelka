import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class UserData(Base):
    __tablename__ = 'user_data'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_name = sa.Column(sa.Text, nullable=False)
    password = sa.Column(sa.Text, nullable=False)


class Albums(Base):
    __tablename__ = 'albums'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user_data.id'))
    album_name = sa.Column(sa.Text)
    images = sa.Column(sa.Text)
