"""Add tokens and services

Revision ID: 21f00fbaf7b9
Revises: fbae07a739a8
Create Date: 2020-09-29 16:37:40.948651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "21f00fbaf7b9"
down_revision = "fbae07a739a8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "services",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tokens",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("value", sa.String(length=255), nullable=False),
        sa.Column("service_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(["service_id"], ["services.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_tokens_service_id"), "tokens", ["service_id"], unique=False
    )
    op.create_table(
        "user_tokens",
        sa.Column("user_id", sa.BigInteger(), nullable=True),
        sa.Column("token_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(["token_id"], ["tokens.id"],),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"],),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_tokens")
    op.drop_table("tokens")
    op.drop_table("services")
    # ### end Alembic commands ###
