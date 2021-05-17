from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__, template_folder="C:\\Users\\Vitor\\Desktop\\Atividades Complementares\\Ambiente_Virtual\\application\\View\\Templates", static_folder="C:\\Users\Vitor\\Desktop\\Atividades Complementares\\Ambiente_Virtual\\application\\View\\Statics")
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from application.Controller import default