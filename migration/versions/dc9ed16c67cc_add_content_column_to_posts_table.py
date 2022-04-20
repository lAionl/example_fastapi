"""Add content column to posts table.

Revision ID: dc9ed16c67cc
Revises: 686a72ee995b
Create Date: 2022-04-19 00:47:51.095506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc9ed16c67cc'
down_revision = '686a72ee995b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
      sa.Column("content", sa.String(), nullable=False)
    )


def downgrade():
    op.drop_column("posts", "content")
