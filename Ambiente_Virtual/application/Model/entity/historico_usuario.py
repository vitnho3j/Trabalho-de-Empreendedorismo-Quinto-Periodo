from application import db
from application.Model.entity import usuario
from application.Model.entity import atividade_complementar

class HistoricoAluno(db.Model):
    __tablename__ = "historicos_alunos"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    ac_id = db.Column(db.Integer, db.ForeignKey('acs.id'))
    ac = db.relationship('Atividade', foreign_keys=ac_id)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'))
    aluno = db.relationship('Aluno', foreign_keys=aluno_id)

    def __init__(self, ac_id, aluno_id):
        ac_id = ac_id
        aluno_id = aluno_id

    def __repr__(self):
        return "<User %r>" % self.id