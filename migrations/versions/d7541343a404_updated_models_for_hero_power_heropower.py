"""Updated models for Hero, Power, HeroPower

Revision ID: d7541343a404
Revises: 253712084e2a
Create Date: 2025-04-01 17:13:36.277776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7541343a404'
down_revision = '253712084e2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('strength',
               existing_type=sa.VARCHAR(length=7),
               type_=sa.String(length=20),
               existing_nullable=False)

    with op.batch_alter_table('powers', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=250),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('powers', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('strength',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=7),
               existing_nullable=False)

    # ### end Alembic commands ###
