"""Add foreign-key to posts table.

Revision ID: baebc4205c17
Revises: eaaa4bddc00c
Create Date: 2022-04-19 01:08:31.693447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baebc4205c17'
down_revision = 'eaaa4bddc00c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
      sa.Column("owner_id", sa.Integer(), nullable=False)
    )

    op.create_foreign_key(
      "posts_users_fk",
      source_table="posts",
      referent_table="users",
      local_cols=["owner_id"],
      remote_cols=["id"],
      ondelete="CASCADE"
    )


def downgrade():
  op.drop_constraint("posts_users_fk", table_name="posts")
  op.drop_column("posts", "owner_id")

