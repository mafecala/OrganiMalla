from flask import Blueprint, redirect, render_template, request, url_for
from .models import Carrera
from . import db

carreras = Blueprint('carreras', __name__)


@carreras.route("/index_carreras")
def index_carreras():
    carreras = Carrera.query.all()
    return render_template("index_carreras.html", carreras=carreras)


@carreras.route("/add_carrera", methods=['POST'])
def add_carrera():
    nombre = request.form['nombre']
    materias = 'a'
    codigo = request.form['codigo']
    creditos = request.form['creditos']
    coordinador = request.form['coordinador']
    ecoordinador = request.form['ecoordinador']

    new_carrera = Carrera(nombre, materias, codigo,
                          creditos, coordinador, ecoordinador)

    db.session.add(new_carrera)
    db.session.commit()

    return redirect(url_for('carreras.index_carreras'))


@carreras.route("/edit_carrera/<id>", methods=['POST', 'GET'])
def edit_carrera(id):
    if request.method == 'POST':
        carrera = Carrera.query.get(id)
        carrera.nombre = request.form["nombre"]
        carrera.codigo = request.form["codigo"]
        carrera.creditos = request.form["creditos"]
        carrera.coordinador = request.form["coordinador"]
        carrera.ecoordinador = request.form["ecoordinador"]
        db.session.commit()

        return redirect(url_for("carreras.index_carreras"))

    carrera = Carrera.query.get(id)

    return render_template("edit_carrera.html", carrera=carrera)


@carreras.route("/delete_carrera/<id>")
def delete_carrera(id):
    carrera = Carrera.query.get(id)
    db.session.delete(carrera)
    db.session.commit()

    return redirect(url_for('carreras.index_carreras'))
