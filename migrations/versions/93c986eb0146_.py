"""empty message

Revision ID: 93c986eb0146
Revises: 0329a2523d00
Create Date: 2021-11-04 14:21:03.129324

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '93c986eb0146'
down_revision = '0329a2523d00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Name', sa.String(length=100), nullable=True),
    sa.Column('abilities', sa.String(length=100), nullable=True),
    sa.Column('base_experience', sa.String(length=100), nullable=True),
    sa.Column('sprite', sa.String(length=100), nullable=True),
    sa.Column('hp', sa.String(length=100), nullable=True),
    sa.Column('attack', sa.String(length=100), nullable=True),
    sa.Column('defense', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('abilities', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('base_experience', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('sprite', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('hp', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('attack', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('defense', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    op.drop_table('pokemon')
    # ### end Alembic commands ###
