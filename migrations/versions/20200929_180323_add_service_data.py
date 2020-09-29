"""Add service data

Revision ID: dad81eb35d67
Revises: 21f00fbaf7b9
Create Date: 2020-09-29 18:03:23.710924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dad81eb35d67"
down_revision = "21f00fbaf7b9"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO services (name, description) VALUES ("toggl", "toggl - time tracking software"), ("exist", "exist - your life in stats");
        """
    )


def downgrade():
    pass
