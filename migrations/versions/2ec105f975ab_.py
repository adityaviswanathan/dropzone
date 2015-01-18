"""empty message

Revision ID: 2ec105f975ab
Revises: None
Create Date: 2015-01-17 15:28:03.499248

"""

# revision identifiers, used by Alembic.
revision = '2ec105f975ab'
down_revision = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drops',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('data_type', sa.Enum('text', 'photo', 'video', name='data_types'), nullable=True),
    sa.Column('data_payload', sa.Text(), nullable=True),
    sa.Column('numviews', sa.Integer(), nullable=True),
    sa.Column('restrictions', sa.Enum('self', 'friends', 'public', name='restriction_types'), nullable=True),
    sa.Column('viewcap', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('teaser', sa.Text(), nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT'), nullable=True),
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