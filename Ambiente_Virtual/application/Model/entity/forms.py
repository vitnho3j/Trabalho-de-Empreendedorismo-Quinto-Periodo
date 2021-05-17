from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    matricula = IntegerField("matricula", validators=[DataRequired()])
    curso = StringField("curso", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")