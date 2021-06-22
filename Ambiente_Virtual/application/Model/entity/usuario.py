from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from application.Model.entity.cursos import Curso
from datetime import timezone
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    aluno = Aluno.query.filter_by(matricula=user_id).first()
    if aluno:
        return aluno
    else:
        administrador = Administrador.query.filter_by(matricula=user_id).first()
        return administrador

class Aluno(db.Model, UserMixin):
    __tablename__ = "alunos"

    nome = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    matricula = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)  
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    curso = db.relationship('Curso', foreign_keys=curso_id)
    horas_ac = db.Column(db.Integer)
    quantidade_ac = db.Column(db.Integer)


    def __init__(self, nome, cpf, matricula, username, password, curso_id):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.username = username
        self.password = password
        self.curso_id = curso_id
        self.horas_ac = 0
        self.quantidade_ac = 0
        self.password = generate_password_hash(password)


    def __repr__(self):
        return "<User %r>" % self.matricula

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def utc_to_local(utc_dt):
            return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


class Administrador(db.Model, UserMixin):
    __tablename__ = "administradores"

    nome = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    matricula = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.Integer)
    password = db.Column(db.String)

    def __init__(self, nome, cpf, matricula, username, password):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "<User %r>" % self.matricula

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def get_class(self):
        return self.__class__


