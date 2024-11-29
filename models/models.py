##Proyecto 3 - Edna Milena Chaparro Perez

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    clave = db.Column(db.String(50), nullable=False)
    administrador = db.Column(db.Integer, nullable=False, default=0)
    empleado = db.Column(db.Integer, nullable=False, default=0)


class Ingrediente(db.Model):
    __tablename__ = "ingredientes"
    id_ingrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    contador = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=True)
    calorias = db.Column(db.Integer, nullable=True)
    vegetariano = db.Column(db.Boolean, nullable=False)

    def __init__(self, id_ingrediente, nombre, contador, precio, calorias, vegetariano):
        self.id_ingrediente = id_ingrediente
        self.nombre = nombre
        self.contador = contador
        self.precio = precio
        self.calorias = calorias
        self.vegetariano = vegetariano

    def save(self):
        if not self.id_ingrediente:
            db.session.add(self)
        db.session.commit()


class Producto(db.Model):
    __tablename__ = "productos"
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def save(self):
        if not self.id_producto:
            db.session.add(self)
        db.session.commit()