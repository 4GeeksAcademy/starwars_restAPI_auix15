"""empty message

Revision ID: 4da85a53ef2c
Revises: a5cffa318ac2
Create Date: 2024-12-18 12:16:36.306686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da85a53ef2c'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('fav',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_character', sa.Integer(), nullable=True),
    sa.Column('id_planet', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_character'], ['character.id'], ),
    sa.ForeignKeyConstraint(['id_planet'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('firstname', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('lastname', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('phone', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('date')
        batch_op.drop_column('phone')
        batch_op.drop_column('address')
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')
        batch_op.drop_column('username')

    op.drop_table('fav')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
