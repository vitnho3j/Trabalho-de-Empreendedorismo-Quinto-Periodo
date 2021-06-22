from application import db

class AlunoAtividades(db.Model):
    __tablename__= "aluno_acs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('alunos.matricula'))
    aluno = db.relationship('Aluno', foreign_keys=id_aluno)
    id_ac = db.Column(db.Integer, db.ForeignKey('acs.id'))
    atividade = db.relationship('Atividade', foreign_keys=id_ac)
    status = db.Column(db.String, default = 'Não enviada')

    def __init__(self, id_aluno, id_ac):
        self.id_aluno = id_aluno
        self.id_ac = id_ac

    def __repr__(self):
        return "<User %r>" % self.id

    def set_status(self, status):
        self.status = status