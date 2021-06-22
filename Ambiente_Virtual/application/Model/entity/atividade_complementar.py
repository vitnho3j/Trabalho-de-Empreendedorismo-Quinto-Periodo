from sqlalchemy.orm import backref
from application import db



class Atividade(db.Model):
    __tablename__= "acs"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    nome = db.Column(db.String)
    categoria = db.Column(db.String)
    horas = db.Column(db.Integer)

    def __init__(self, nome, categoria, horas):
        self.nome = nome
        self.categoria = categoria
        self.horas = horas

    def get_atividade(self, id):
        return self.id
        
