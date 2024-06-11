"""Add nutrition facts columns to Recipe model

Revision ID: 34841d00f0af
Revises: 
Create Date: 2024-06-11 20:19:37.091515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34841d00f0af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('calories', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('protein', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('carbohydrates', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('fat', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_column('fat')
        batch_op.drop_column('carbohydrates')
        batch_op.drop_column('protein')
        batch_op.drop_column('calories')

    # ### end Alembic commands ###
