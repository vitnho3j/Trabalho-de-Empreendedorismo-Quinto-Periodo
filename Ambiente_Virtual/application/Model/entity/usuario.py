from application import db
from application.Model.entity.historico_usuario import HistoricoAluno


class Pessoa(db.Model):
    nome = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    data_nascimento = db.Column(db.Date)

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    class Meta:
        abstract=True

class Aluno(Pessoa):
    __tablename__ = "alunos"

    OPCOES = (
        ('Engenharia de Software', 'EngSoftware'),
        ('Engenharia Civil', 'EngCivil'),
        ('Engenharia Química', 'EngQuimica'),
        ('Psicologia', 'Psicologia'),
        ('Medicina', 'Medicina'),
        ('Enfermagem', 'Enfermagem'),
        ('Veterinária', 'Veterinaria'),
    ) 

    matricula = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(matricula)
    password = db.Column(db.String)
    curso = db.Column(db.String, choices=OPCOES)
    horas_ac = db.Column(db.Float)
    historico_id = db.Column(db.Interger, db.ForeignKey('historico.id'))
    historico = db.relationship('HistoricoAluno', foreign_keys=historico_id)
    

    def __init__(self, username, password, curso_id, horas_ac):
        self.username = username
        self.password = password
        self.curso_id = curso_id
        self.horas_ac = horas_ac

    def __repr__(self):
        return "<User %r>" % self.matricula


class Administrador(Pessoa):
    __tablename__ = "administradores"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(id)
    password = db.Column(db.String)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.id
