"""add user table

Revision ID: 5241d922d5c7
Revises: 91ffc42f0e82
Create Date: 2022-03-13 21:28:10.899076

"""
from ast import Num
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5241d922d5c7'
down_revision = '91ffc42f0e82'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
