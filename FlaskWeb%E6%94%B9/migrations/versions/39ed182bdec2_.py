"""empty message

Revision ID: 39ed182bdec2
Revises: 8f75892a26c5
Create Date: 2024-03-23 19:14:17.008013

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '39ed182bdec2'
down_revision = '8f75892a26c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('username', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('password', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('username'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###