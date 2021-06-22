from enum import unique
from sqlalchemy.sql.schema import ForeignKey
from application import db
from application.Model.entity.cursos import Curso
from application.Model.entity.atividade_complementar import Atividade

def padrao():
    return False

lista = []

class CursosDisponiveis(db.Model):
    __tablename__= "cursos_acs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    atividade_id = db.Column(db.Integer, db.ForeignKey('acs.id'), unique=False)
    atividade = db.relationship('Atividade', foreign_keys=atividade_id)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), unique=False)
    curso = db.relationship('Curso', foreign_keys=curso_id)
    
    def __init__(self, atividade_id, curso_id):
        self.atividade_id = atividade_id
        self.curso_id = curso_id

    '''
    def set_True(self, curso):
        curso_nome = Curso.query.filter_by(nome = curso).first()
        curso = CursosDisponiveis.query.order_by(curso_nome).first()
        curso.status = True
        db.session.add(curso)
        db.session.commit()
        return
    '''
