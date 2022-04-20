"""Create posts table.

Revision ID: 686a72ee995b
Revises: 
Create Date: 2022-04-14 09:26:32.971661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '686a72ee995b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts",
    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
