""" add content column to posts table

Revision ID: 91ffc42f0e82
Revises: 1e484a663ef7
Create Date: 2022-03-12 19:10:03.171520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91ffc42f0e82'
down_revision = '1e484a663ef7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
