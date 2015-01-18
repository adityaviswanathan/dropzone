"""empty message

Revision ID: 10688d0d13c7
Revises: None
Create Date: 2015-01-18 01:50:11.700816

"""

# revision identifiers, used by Alembic.
revision = '10688d0d13c7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drops',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('data_type', sa.Enum('text', 'photo', 'video', 'payment', name='data_types'), nullable=True),
    sa.Column('data_payload', sa.Text(), nullable=True),
    sa.Column('numviews', sa.Integer(), nullable=True),
    sa.Column('restrictions', sa.Enum('self', 'friends', 'public', name='restriction_types'), nullable=True),
    sa.Column('viewcap', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('teaser', sa.Text(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pickups',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('drop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['drop_id'], ['drops.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pickups')
    op.drop_table('drops')
    op.drop_table('users')
    ### end Alembic commands ###