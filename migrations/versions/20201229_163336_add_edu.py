"""empty message

Revision ID: ed27005b99b6
Revises: cbf948acdd83
Create Date: 2020-12-29 16:33:36.216926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ed27005b99b6"
down_revision = "cbf948acdd83"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "education_worlds",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("size", sa.BigInteger(), nullable=True),
        sa.Column("population_size", sa.String(length=255), nullable=True),
        sa.Column("minimal_resources", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "education_tiles",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("x", sa.BigInteger(), nullable=True),
        sa.Column("y", sa.BigInteger(), nullable=True),
        sa.Column("world_id", sa.BigInteger(), nullable=False),
        sa.Column("resources", sa.BigInteger(), nullable=True),
        sa.Column("human", sa.Boolean(), nullable=True),
        sa.Column("habitable", sa.Boolean(), nullable=True),
        sa.Column("tile_type", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["world_id"],
            ["education_worlds.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("education_tiles")
    op.drop_table("education_worlds")
    # ### end Alembic commands ###
