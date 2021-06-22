from re import A, T
from flask.globals import g, session
from flask.helpers import send_file
from flask.wrappers import Request
from matplotlib.figure import Figure
from sqlalchemy.orm import query
from werkzeug.datastructures import MultiDict
from wtforms.fields.simple import SubmitField
from application import app, login_manager, db
from flask import render_template, request, redirect, url_for, jsonify, Response
from flask_login import login_user, logout_user, current_user
from application.Model.entity.usuario import Administrador, Aluno
from application.Model.entity.cursos import Curso
from application.Model.entity.atividade_complementar import Atividade
from application.Model.dao.atividade_complementar_DAO import AtividadeDAO
from application.Model.entity.aluno_acs import AlunoAtividades
from application.Model.entity.cursos_acs import CursosDisponiveis
from application.Model.entity.forms import LoginForm
from application import db
from sqlalchemy import and_, or_, desc, func
import json
import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import io
import base64
import random
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mtick


palestras = 0 
semana_academica = 0
seminario = 0
congresso = 0
atividade_cultural = 0
iniciacao_cientifica = 0

@app.route("/index")
@app.route("/")
def index():
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador" 
    return render_template('index.html', redirect=redirect, desc=desc, Atividade = Atividade, tipo = tipo)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if request.method == 'POST': 
        nome = request.form['name']
        cpf = request.form['cpf']
        matricula = request.form['matricula']
        username = request.form['username']
        password = request.form['password']
        curso_nome = request.form['curso']
        curso = Curso.query.filter_by(nome=curso_nome).first()
        user = Aluno(nome, cpf, matricula, username, password, curso.id)
        db.session.add(user)
        db.session.commit()
        return render_template('register.html', form=form, redirect=redirect)

    return render_template('register.html', form=form, Aluno=Aluno, Curso=Curso)

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        matricula = request.form['matricula']
        aluno = Aluno.query.filter_by(matricula=matricula).first()
        db.session.delete(aluno)
        db.session.commit()
        return 'OK'

    return render_template('delete.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST': 
        username = request.form['username']
        pwd = request.form['password']

        user = Aluno.query.filter_by(username=username).first()

        if not user or not user.verify_password(pwd):
            user = Administrador.query.filter_by(username=username).first()
            if not user or not user.verify_password(pwd):
                return redirect(url_for('login', form=form))

            login_user(user)
            return redirect(url_for('index'))

        login_user(user)
        print(user.__class__.__name__)
        return redirect(url_for('index'))
        

    return render_template('login.html', form=form)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', Aluno=Aluno)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/atividades', methods=['GET','POST'])
def atividade():
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador" 
    lista = []
    if request.method == 'POST':
        nome = request.form['nome']
        cursos = request.form.getlist('mycheckbox')
        categoria = request.form['categoria']
        horas = request.form['horas']
        lista.append(cursos)
        atividade = Atividade(nome, categoria, horas)
        db.session.add(atividade)
        db.session.commit()

        for i in cursos:
            curso = Curso.query.filter_by(nome=i).first()
            disponiveis = CursosDisponiveis(atividade.id, curso.id)
            db.session.add(disponiveis)
            db.session.commit()


        return render_template('atividades.html', Curso=Curso, tipo = tipo)

    return render_template('atividades.html', Curso=Curso, tipo=tipo)


@app.route('/curso', methods=['GET', 'POST'])
def curso():
    form = LoginForm()
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador" 
    if request.method == 'POST': 
        nome = request.form['nome']
        carga_ac = request.form['carga_ac']
        user = Curso(nome, carga_ac)
        db.session.add(user)
        db.session.commit()
        return render_template('curso.html', tipo = tipo, form = form)

    return render_template('curso.html', tipo = tipo, form = form)

@app.route('/administrador', methods=['GET', 'POST'])
def administrador():
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador"  
    if request.method == 'POST': 
        nome = request.form['nome']
        cpf = request.form['cpf']
        matricula = request.form['matricula']
        username = request.form['username']
        password = request.form['password']
        user = Administrador(nome, cpf, matricula, username, password)
        db.session.add(user)
        db.session.commit()
        return render_template('administrador.html', tipo=tipo)

    return render_template('administrador.html', tipo=tipo)


@app.route('/atividades/aluno/<id>', methods=['GET', 'POST'])
@app.route('/atividades/aluno', defaults={'id':None}, methods=['GET', 'POST'])

def registrar_atividade(id):  
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador"

    if request.method == 'POST':
        user = current_user.matricula
        atividade_id = AtividadeDAO.search_atividade(id)
        registro = AlunoAtividades(user, atividade_id)
        aluno = Aluno.query.filter_by(matricula=user).first()
        db.session.add(registro)
        db.session.commit()

        return render_template('atividades_aluno.html', CursosDisponiveis=CursosDisponiveis, Atividade=Atividade, tipo=tipo, redirect=redirect, AlunoAtividades=AlunoAtividades, Aluno=Aluno, Curso=Curso, and_=and_)
    
    return render_template('atividades_aluno.html', CursosDisponiveis=CursosDisponiveis, Atividade=Atividade, tipo=tipo, redirect=redirect, AlunoAtividades=AlunoAtividades, Aluno=Aluno, Curso=Curso, and_ = and_)

@app.route('/exibir/atividades/<id>', methods=['POST', 'GET'])
@app.route('/exibir/atividades', defaults={'id':None}, methods=['GET', 'POST'])
 
def enviar_atividade(id):
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador"  
         
    if request.method == 'POST':
        ac = AlunoAtividades.query.filter_by(id=id).first()
        ac.status = "Enviada"
        db.session.add(ac)
        db.session.commit()
        return render_template('exibir_atividades.html', AlunoAtividades=AlunoAtividades, Atividade=Atividade, and_=and_, or_=or_, tipo=tipo)
    print(tipo)
    return render_template('exibir_atividades.html', AlunoAtividades=AlunoAtividades, Atividade=Atividade, and_=and_, or_=or_, tipo=tipo)

@app.route('/validate/<id>', methods=['POST', 'GET'])
@app.route('/validate', defaults={'id':None}, methods=['POST', 'GET'])
def validate(id):
    matricula = 0
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador"  
    if request.method == 'POST':
        variable = request.form.__copy__()
        if variable['acao'] == 'Validar':
            ac = AlunoAtividades.query.filter_by(id=id).first()
            atividade = Atividade.query.filter_by(id = ac.id_ac).first()
            ac.status = "Aprovada"
            aluno = Aluno.query.filter_by(matricula=ac.id_aluno).first()
            aluno.quantidade_ac = aluno.quantidade_ac + 1
            aluno.horas_ac = aluno.horas_ac + atividade.horas
            db.session.add(ac, aluno)
            db.session.commit()
        else:
            ac = AlunoAtividades.query.filter_by(id=id).first()
            ac.status = "Reprovada"
            db.session.add(ac)
            db.session.commit()

        variable = request.form.copy()
        print(ac.status)
        print(variable)
        
        return render_template('atividades_aluno.html', CursosDisponiveis=CursosDisponiveis, Atividade=Atividade, tipo=tipo, redirect=redirect, AlunoAtividades=AlunoAtividades, Aluno=Aluno, Curso=Curso, and_ = and_, matricula = matricula)  


@app.route('/perfil', methods=['GET'])
def perfil():
    user = current_user.get_id()
    if Aluno.query.filter_by(matricula=user).first():
        tipo = "Aluno"
    else:
        tipo = "Administrador" 
    if tipo == "Administrador":
        render_template('index.html', redirect=redirect, desc=desc, Atividade = Atividade) 
    else:
        global palestras
        global semana_academica
        global seminario
        global congresso
        global atividade_cultural
        global iniciacao_cientifica
        palestras = 0 
        semana_academica = 0
        seminario = 0
        congresso = 0
        atividade_cultural = 0
        iniciacao_cientifica = 0

        for i in AlunoAtividades.query.filter_by(id_aluno=current_user.matricula):
            if i.status == "Aprovada":
                atividade = Atividade.query.filter_by(id = i.id_ac).first()
                if atividade.categoria == "Palestra" : 
                    palestras = palestras + 1
                if atividade.categoria == "Semana Acadêmica":
                    semana_academica = semana_academica + 1
                if atividade.categoria == "Seminário":
                    seminario = seminario + 1
                if atividade.categoria == "Congresso" :
                    congresso = congresso + 1
                if atividade.categoria == "Atividade Cultiral":
                    atividade_cultural = atividade_cultural + 1
                if atividade.categoria == "Iniciação Científica":
                    iniciacao_cientifica = iniciacao_cientifica + iniciacao_cientifica
            else:
                pass

        x_list = [palestras, semana_academica, seminario, congresso, atividade_cultural, iniciacao_cientifica]
        labels_list = ['Palestras', 'Semana Acadêmica', 'Seminário', 'Congresso', 'Atividade Cultural', 'Iniciação Científica']
        pyplot.pie(x_list, labels=labels_list, autopct='%1.1f%%', startangle= 90, shadow=True)
        pyplot.title("Porcentagem de Atividades Complementares")
        return render_template('perfil.html', AlunoAtividades=AlunoAtividades, Atividade=Atividade, func=func, palestras = palestras, semana_academica=semana_academica, seminario=seminario, congresso=congresso, atividade_cultural= atividade_cultural, iniciacao_cientifica = iniciacao_cientifica, tipo=tipo)
    return render_template('perfil.html', AlunoAtividades=AlunoAtividades, Atividade=Atividade, func=func, palestras = palestras, semana_academica=semana_academica, seminario=seminario, congresso=congresso, atividade_cultural= atividade_cultural, iniciacao_cientifica = iniciacao_cientifica, tipo = tipo)


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig, ax = pyplot.subplots(figsize = (11,6))
    fig.patch.set_facecolor('#E8E5DA')

    
    ys = [palestras, semana_academica, seminario, congresso, atividade_cultural, iniciacao_cientifica]
    xs = ['Palestras', 'Semana Acadêmica', 'Seminário', 'Congresso', 'Atividade Cultural', 'Iniciação Científica']

    ax.bar(xs, ys, color = "#304C89")

    pyplot.xticks()
    pyplot.title("Classificação da categoria e contabilização das suas atividades realizadas")
    pyplot.ylabel("Números de Atividades Concluidas", size = 20)
    total = sum(ys)

    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy() 
        ax.annotate(f'{height}', (x + width/2, y + height*1.02), ha='center')

    for p in ax.patches:
        height = p.get_height()
        percentage = '{:.1f}%'.format(100 * (height / total))
        x = p.get_x() + p.get_width() / 2
        y = p.get_y()
        ax.annotate(percentage, (x, y), ha='center')

        print(percentage) 
    return fig

@app.route('/about')
def about():
    return render_template('sobre.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


