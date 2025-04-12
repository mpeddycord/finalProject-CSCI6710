from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import date
from app.search import add_to_index, remove_from_index, query_index

class SearchableMixin:
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return [], 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        query = sa.select(cls).where(cls.id.in_(ids)).order_by(db.case(*when, value=cls.id))
        return db.session.scalars(query), total
    
    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in db.session.scalars(sa.select(cls)):
            add_to_index(cls.__tablename__, obj)
        
db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(255))
    avatar_url: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)

    def __repr__(self):
        return '<User {}'.format(self.name)

class Post(SearchableMixin, db.Model):
    __searchable__ = ['body']
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
    rating: so.Mapped[str] = so.mapped_column(sa.String(5))
    box_office: so.Mapped[str] = so.mapped_column(sa.String(25))
    director: so.Mapped[str] = so.mapped_column(sa.String(255))
    description: so.Mapped[str] = so.mapped_column(sa.String(255))
    release_date: so.Mapped[str] = so.mapped_column(sa.String(25))
    budget: so.Mapped[str] = so.mapped_column(sa.String(25))
    post_date: so.Mapped[date] =  so.mapped_column(sa.Date)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('User.id'), nullable=False)
    author = so.relationship("User", foreign_keys=[author_id], primaryjoin="User.id == Movie.author_id")

class MovieMoment(db.Model):
    __tablename__ = 'MovieMoment'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(500))
    movie_id = sa.Column(sa.Integer, sa.ForeignKey('Movie.id'), nullable=False)
    movie = so.relationship("Movie", foreign_keys=[movie_id], primaryjoin="Movie.id == MovieMoment.movie_id")

class MovieReason(db.Model):
    __tablename__ = 'MovieReason'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    type: so.Mapped[str] = so.mapped_column(sa.String(1), index=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(500))
    movie_id = sa.Column(sa.Integer, sa.ForeignKey('Movie.id'), nullable=False)
    movie = so.relationship("Movie", foreign_keys=[movie_id], primaryjoin="Movie.id == MovieReason.movie_id")