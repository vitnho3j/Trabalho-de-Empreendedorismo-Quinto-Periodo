from application import db


class Curso(db.Model):
    __tablename__="cursos"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    nome = db.Column(db.String)
    carga_ac = db.Column(db.Integer)

    def __init__(self, nome, carga_ac):
        self.nome = nome
        self.carga_ac = carga_ac

    def __repr__(self):
        return "<User %r>" % self.nome
        