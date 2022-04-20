"""Add user table.

Revision ID: eaaa4bddc00c
Revises: dc9ed16c67cc
Create Date: 2022-04-19 00:52:55.823280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaaa4bddc00c'
down_revision = 'dc9ed16c67cc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
      sa.Column("id", sa.Integer(), nullable=False),
      sa.Column("email", sa.String(), nullable=False),
      sa.Column("password", sa.String(), nullable=False),
      sa.Column("creatted_at", sa.TIMESTAMP(timezone=True),
        server_default=sa.text("now()"), nullable=False),
      sa.PrimaryKeyConstraint("id"),
      sa.UniqueConstraint("email")
    )


def downgrade():
    op.drop_table("users")
