"""add last few columns to posts table

Revision ID: ec5535fb45f7
Revises: fc6f00a1dbfb
Create Date: 2022-03-16 12:48:47.097946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec5535fb45f7'
down_revision = 'fc6f00a1dbfb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default="TRUE"),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
