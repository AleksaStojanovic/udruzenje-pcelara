"""add tag model

Revision ID: 30b6d27154b5
Revises: 845624061a31
Create Date: 2021-05-18 14:54:08.062655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30b6d27154b5'
down_revision = '845624061a31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags_association',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags_association')
    op.drop_table('tag')
    # ### end Alembic commands ###