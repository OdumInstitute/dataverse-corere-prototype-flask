"""empty message

Revision ID: 6f2ba2c1cd62
Revises: 8a3b3e73c09f
Create Date: 2019-04-16 10:09:43.738795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f2ba2c1cd62'
down_revision = '8a3b3e73c09f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('given_name', sa.String(length=250), nullable=True),
    sa.Column('family_name', sa.String(length=250), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Catalog')
    op.drop_table('Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Users_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('given_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('family_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('role', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Catalog',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Catalog_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], name='Catalog_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Catalog_pkey')
    )
    op.drop_table('catalog')
    op.drop_table('users')
    # ### end Alembic commands ###