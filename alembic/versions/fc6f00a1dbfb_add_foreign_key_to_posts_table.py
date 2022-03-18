""" add foreign-key to posts table

Revision ID: fc6f00a1dbfb
Revises: 5241d922d5c7
Create Date: 2022-03-13 21:39:29.843428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc6f00a1dbfb'
down_revision = '5241d922d5c7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_usrs_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
