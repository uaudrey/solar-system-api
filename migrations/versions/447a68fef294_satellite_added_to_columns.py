"""satellite added to columns

Revision ID: 447a68fef294
Revises: 929de86a0268
Create Date: 2022-11-03 11:43:50.238153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '447a68fef294'
down_revision = '929de86a0268'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('satellite', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'satellite')
    # ### end Alembic commands ###
