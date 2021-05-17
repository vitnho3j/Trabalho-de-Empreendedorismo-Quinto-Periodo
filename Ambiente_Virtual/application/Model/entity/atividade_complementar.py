from application import db


class Atividade(db.Model):
    __tablename__= "acs"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String)
    categoria = db.Column(db.String)

