from datetime import datetime
from sqlalchemy.orm import validates

from flaskr_carved_rock.sqla import sqla

class Post(sqla.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    author_id = sqla.Column(sqla.Integer, sqla.ForeignKey('user.id'), nullable=False)
    author = sqla.relationship('User', backref=sqla.backref('posts', lazy=True))
    created = sqla.Column(sqla.DateTime, nullable=False, default=datetime.utcnow)
    title = sqla.Column(sqla.Text, nullable=False)
    body = sqla.Column(sqla.Text, nullable=False)
    comments = []

    @validates('title')
    def validate_not_empty(self, key, value):
        if not value:
            raise ValueError(f'{key.capitalize()} is required.')
        return value

    def __repr__(self):
        return self.title