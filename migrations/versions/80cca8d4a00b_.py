"""empty message

Revision ID: 80cca8d4a00b
Revises: 53784eb200c8
Create Date: 2022-01-20 05:39:47.870496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80cca8d4a00b'
down_revision = '53784eb200c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('test_col', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'test_col')
    # ### end Alembic commands ###