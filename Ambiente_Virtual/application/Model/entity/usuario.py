from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from application.Model.entity.historico_usuario import HistoricoAluno
from datetime import timezone
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return Aluno.query.filter_by(matricula=user_id).first()

class Aluno(db.Model, UserMixin):
    __tablename__ = "alunos"

    nome = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    matricula = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    curso = db.Column(db.String)
    horas_ac = db.Column(db.Float)
    historico_id = db.Column(db.Integer, db.ForeignKey('historicos_alunos.id'))
    historico = db.relationship('HistoricoAluno', foreign_keys=historico_id)
    

    def __init__(self, nome, cpf, matricula, username, password, curso_id):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.username = username
        self.password = generate_password_hash(password)
        self.curso_id = curso_id

    def __repr__(self):
        return "<User %r>" % self.matricula

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def utc_to_local(utc_dt):
            return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)



class Administrador(db.Model):
    __tablename__ = "administradores"

    nome = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    matricula = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.Integer)
    password = db.Column(db.String)

    def __init__(self, nome, cpf, id, username, password):
        self.nome = nome
        self.cpf = cpf
        self.id = id
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "<User %r>" % self.id
