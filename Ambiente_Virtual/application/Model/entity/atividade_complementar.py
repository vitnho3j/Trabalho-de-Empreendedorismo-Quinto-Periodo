from application import db
from application.Model.entity import usuario

class Atividade(db.Model):
    __tablename__= "acs"
    OPCOES = (
        ('Palestra', 'Palestra'),
        ('Semana Acadêmica', 'Semana_Acadêmica'),
        ('Seminário', 'Seminario'),
        ('Congresso', 'Congresso'),
        ('Atividade Cultural', 'Atividade_Cultural'),
        ('Publicação em Revista Científica', 'Publicacao'),
        ('Integralização de cursos de extensão', 'Integralizacao'),
        ('Iniciação Científica', 'Iniciacao'),

    ) 
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String)
    categoria = db.Column(db.String, choices=OPCOES)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id')) 
    aluno = db.Column(db.relationship('Aluno', foreign_keys=aluno_id))
