from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(255))

    def __repr__(self):
        return '<User {}'.format(self.name)
