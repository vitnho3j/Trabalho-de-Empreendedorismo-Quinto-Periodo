"""empty message

Revision ID: 8dd7230b470f
Revises: 
Create Date: 2021-05-16 13:18:53.585207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dd7230b470f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('acs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('categoria', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('administradores',
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('cpf', sa.String(), nullable=True),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('alunos',
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('cpf', sa.String(), nullable=True),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('matricula', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('curso', sa.String(), nullable=True),
    sa.Column('horas_ac', sa.Float(), nullable=True),
    sa.Column('historico_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['historico_id'], ['historicos_alunos.id'], ),
    sa.PrimaryKeyConstraint('matricula'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('matricula'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('historicos_alunos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ac_id', sa.Integer(), nullable=True),
    sa.Column('aluno_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ac_id'], ['acs.id'], ),
    sa.ForeignKeyConstraint(['aluno_id'], ['alunos.matricula'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historicos_alunos')
    op.drop_table('alunos')
    op.drop_table('administradores')
    op.drop_table('acs')
    # ### end Alembic commands ###