from application import app, login_manager, db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application.Model.entity.usuario import Aluno
from application.Model.entity.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', redirect=redirect)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    cadastrado = "Você foi cadastrado com sucesso, logue-se em nosso sistema"
    if request.method == 'POST': 
        nome = request.form['name']
        cpf = request.form['cpf']
        matricula = request.form['matricula']
        username = request.form['username']
        password = request.form['password']
        curso = request.form['curso']
        user = Aluno(nome, cpf, matricula, username, password, curso)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('register', cadastrado=cadastrado, redirect=redirect)) and "Você foi cadastrado com sucesso, logue-se em nosso sistema"

    return render_template('register.html', form=form)

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
    if request.method == 'POST': 
        username = request.form['username']
        pwd = request.form['password']

        aluno = Aluno.query.filter_by(username=username).first()

        if not aluno or not aluno.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(aluno)
        return redirect(url_for('index'))

    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
