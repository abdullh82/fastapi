""" create posts table

Revision ID: 1e484a663ef7
Revises: 
Create Date: 2022-03-12 18:29:08.015006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e484a663ef7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts",sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
      sa.Column('title',sa.String(),nullable=False))


def downgrade():
    op.drop_table("posts")
