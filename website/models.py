from . import db
#from flask_login import UserMixin

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50))
    correo_usuario = db.Column(db.String(50), unique=True)
    carrera_usuario = db.Column(db.String(15))
    materias_usuario = db.relationship('Materia', backref='usuario', lazy=True)


class Materia(db.Model):
    id_materia = db.Column(db.Integer, primary_key=True)
    nombre_materia = db.Column(db.String(100))
    codigo_materia = db.Column(db.String(100))
    creditos_materia = db.Column(db.String(100))
    area_materia = db.Column(db.String(100))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'),
        nullable=False)

    def __init__(self, nombre_materia, codigo_materia, creditos_materia, area_materia):
        self.nombre_materia = nombre_materia
        self.codigo_materia = codigo_materia
        self.creditos_materia = creditos_materia
        self.area_materia = area_materia

class Carrera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    materias = db.Column(db.String(10000))
    codigo = db.Column(db.String(100))
    creditos = db.Column(db.String(100))
    coordinador = db.Column(db.String(100))
    ecoordinador = db.Column(db.String(100))
    
    def __init__(self, nombre, materias, codigo, creditos, coordinador, ecoordinador):
        self.nombre = nombre
        self.materias = materias
        self.codigo = codigo
        self.creditos = creditos
        self.coordinador = coordinador
        self.ecoordinador = ecoordinador
