"""empty message

Revision ID: 422cb51eed2f
Revises: 46c8f054a7be
Create Date: 2019-04-16 11:17:46.449143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '422cb51eed2f'
down_revision = '46c8f054a7be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###