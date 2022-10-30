from . import db
#from flask_login import UserMixin

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50), unique=True)
    carrera = db.Column(db.String(15))