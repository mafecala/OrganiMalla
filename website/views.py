from distutils import core
from flask import Blueprint, render_template, request, flash
from .models import Usuario
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")


@views.route('/materias', methods=['POST'])
def materias():
    if request.method == 'POST':
        nombreUsuario = request.form.get('nombreUsuario')
        correo = request.form.get('correo')
        carrera = request.form.get('carrera')

        if not nombreUsuario or not correo or not carrera:
            return "<h1>Debes llenar todos los campos</h1>"
        elif Usuario.query.filter_by(correo=correo).count() > 0:
            return "<h1>Correo repetido</h1>"
        else:
            nuevoUsuario = Usuario(nombre=nombreUsuario, correo=correo, carrera=carrera)
            db.session.add(nuevoUsuario)
            db.session.commit()
    
    usuarios = Usuario.query.all()
    return render_template("usuarios.html", usuarios=usuarios)

