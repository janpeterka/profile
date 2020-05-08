"""empty message

Revision ID: ebc47c4a3634
Revises: 
Create Date: 2020-05-08 13:35:24.537004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebc47c4a3634'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bunkrs')
    op.add_column('poezie', sa.Column('photo_path', sa.String(length=511), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poezie', 'photo_path')
    op.create_table('bunkrs',
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('sale_date', sa.VARCHAR(length=255), nullable=True),
    sa.Column('link', sa.VARCHAR(length=255), nullable=True),
    sa.Column('katastr', sa.VARCHAR(length=255), nullable=True),
    sa.Column('obec', sa.VARCHAR(length=255), nullable=True),
    sa.Column('kraj', sa.VARCHAR(length=255), nullable=True),
    sa.Column('uzemi', sa.VARCHAR(length=255), nullable=True),
    sa.Column('min_sale_price', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('offer_type', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###
