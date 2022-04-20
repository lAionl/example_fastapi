"""Add last few columns to posts table.

Revision ID: 37a8e28e2651
Revises: baebc4205c17
Create Date: 2022-04-19 01:17:20.277875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a8e28e2651'
down_revision = 'baebc4205c17'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
      sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="True"
      ),
    )

    op.add_column("posts",
      sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text("NOW()")
      ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
