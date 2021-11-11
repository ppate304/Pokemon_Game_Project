"""empty message

Revision ID: 685e123cb50e
Revises: 0e4d9d05bcb9
Create Date: 2021-11-04 16:05:02.836140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '685e123cb50e'
down_revision = '0e4d9d05bcb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=150), nullable=True))
    op.drop_column('user', 'first')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
