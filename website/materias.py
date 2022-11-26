from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Materia
from . import db

materias = Blueprint('materias', __name__)

@materias.route('/index_materias')
def index():
    materias = Materia.query.all()
    return render_template('index_materias.html', materias=materias)

@materias.route('/new', methods=['POST'])
def add_materia():
    nombre_materia = request.form['nombre_materia']
    codigo_materia = request.form['codigo_materia']
    creditos_materia = request.form['creditos_materia']
    area_materia = request.form['area_materia']

    new_materia = Materia(nombre_materia,codigo_materia,creditos_materia, area_materia)

    db.session.add(new_materia)
    db.session.commit()

    flash("Materia añadida")

    return redirect(url_for('materias.index'))

@materias.route('/update/<id_materia>', methods = ['POST', 'GET'])
def update(id_materia):
    materia = Materia.query.get(id_materia)
    
    if request.method == 'POST':
        materia.nombre_materia = request.form['nombre_materia']
        materia.codigo_materia = request.form['codigo_materia']
        materia.creditos_materia = request.form['creditos_materia']
        materia.area_materia = request.form['area_materia']

        db.session.commit()

        flash('Materia actualizada')

        return redirect(url_for('materias.index')) 

    return render_template("update.html", materia = materia)

@materias.route('/delete/<id_materia>')
def delete(id_materia):
    materia = Materia.query.get(id_materia)
    db.session.delete(materia)
    db.session.commit()

    flash('Materia eliminada')

    return redirect(url_for('materias.index'))



@materias.route("/seleccionar_materias", methods=['GET', 'POST'])
def seleccionar_materias():
    materias = Materia.query.all()
    if request.method == 'POST':
        materias_seleccionadas = request.form.getlist("a")
        return redirect(url_for("home"))
    return render_template("select.html",materias=materias)


@materias.route("/home")
def home():
    return render_template("home.html")