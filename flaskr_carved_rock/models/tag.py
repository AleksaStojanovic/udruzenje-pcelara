from flaskr_carved_rock.sqla import sqla

tags_association = sqla.Table('tags_association',
    sqla.Column('tag_id', sqla.Integer, sqla.ForeignKey('tag.id')),
    sqla.Column('post_id', sqla.Integer, sqla.ForeignKey('post.id'))
)

class Tag(sqla.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(64), nullable=False)
    posts = sqla.relationship('Post', secondary=tags_association, backref=sqla.backref('tags', lazy=True))

    def __repr__(self):
        return self.name