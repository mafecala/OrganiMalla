from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def crear_app():
    # Crear app y base de datos
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'poo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Importar vistas de la app
    from .views import views
    from .auth import auth
    from .materias import materias
    from .carreras import carreras

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    app.register_blueprint(materias, url_prefix = '/')
    app.register_blueprint(carreras, url_prefix = '/')

    from .models import Usuario

    crear_database(app)

    return app

def crear_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Base de datos creada')