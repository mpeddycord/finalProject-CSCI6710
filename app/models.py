from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import date

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(255))
    avatar_url: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)

    def __repr__(self):
        return '<User {}'.format(self.name)

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    image_url: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    stub: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(2000))
    date_created: so.Mapped[date] =  so.mapped_column(sa.Date)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('User.id'), nullable=False)
    author = so.relationship("User", foreign_keys=[author_id], primaryjoin="User.id == Post.author_id")

class Movie(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    genre: so.Mapped[str] = so.mapped_column(sa.String(50))
    runtime: so.Mapped[str] = so.mapped_column(sa.String(25))
    image_url: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    position: so.Mapped[str] = so.mapped_column(sa.String(10))
    rating: so.Mapped[str] = so.mapped_column(sa.String(4))
    box_office: so.Mapped[str] = so.mapped_column(sa.String(25))
    director: so.Mapped[str] = so.mapped_column(sa.String(255))
    release_date: so.Mapped[str] = so.mapped_column(sa.String(25))
    budget: so.Mapped[str] = so.mapped_column(sa.String(25))
    post_date: so.Mapped[date] =  so.mapped_column(sa.Date)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('User.id'), nullable=False)
    author = so.relationship("User", foreign_keys=[author_id], primaryjoin="User.id == Movie.author_id")