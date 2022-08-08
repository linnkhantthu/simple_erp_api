"""empty message

Revision ID: b03f1cc606dc
Revises: 
Create Date: 2022-08-08 22:54:49.301563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b03f1cc606dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=60), nullable=False),
    sa.Column('lastName', sa.String(length=60), nullable=False),
    sa.Column('mail', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mail')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productName', sa.String(length=60), nullable=False),
    sa.Column('contains', sa.String(length=60), nullable=False),
    sa.Column('unit', sa.String(length=150), nullable=False),
    sa.Column('price', sa.String(length=150), nullable=False),
    sa.Column('qty', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('user')
    # ### end Alembic commands ###