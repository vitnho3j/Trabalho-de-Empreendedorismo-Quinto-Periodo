from application.Model.entity.cursos import Curso
from application.Model.entity.atividade_complementar import Atividade
from application import db

class AtividadeDAO():
    #def cursos_disponiveis(self, lista):
        #for i in lista:
            #curso = CursosDisponiveis.query.filter_by(nome = i).first()
            #setar = Curso.set_True(curso)
            #db.session.add(setar)
            #db.session.commit()

    def search_atividade(id):
       return Atividade.query.filter_by(id = id).first().id
