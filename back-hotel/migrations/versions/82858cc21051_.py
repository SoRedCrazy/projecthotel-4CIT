"""empty message

Revision ID: 82858cc21051
Revises: 7151924d8b4a
Create Date: 2024-02-23 20:45:51.318096

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '82858cc21051'
down_revision = '7151924d8b4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('D', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('create_at', sa.DateTime(timezone=True), nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('create_at')
        batch_op.drop_column('D')

    # ### end Alembic commands ###