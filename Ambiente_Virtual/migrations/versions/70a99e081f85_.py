"""empty message

Revision ID: 70a99e081f85
Revises: 8dd7230b470f
Create Date: 2021-05-16 16:08:26.311006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70a99e081f85'
down_revision = '8dd7230b470f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('administradores', 'data_nascimento')
    op.drop_column('alunos', 'data_nascimento')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alunos', sa.Column('data_nascimento', sa.DATE(), nullable=True))
    op.add_column('administradores', sa.Column('data_nascimento', sa.DATE(), nullable=True))
    # ### end Alembic commands ###