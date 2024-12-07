# Import
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import mysql.connector

# Instancia +config
# load_dotenv()
app = Flask(__name__, template_folder="views")

# Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root:@localhost:3306/' + os.path.join('usuarios_db.db')
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root:@localhost:3306/' + os.path.join('usuarios_db.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
secret_key = os.urandom(24)
app.config["SECRET_KEY"] = secret_key

login_manager = LoginManager(app)

db = SQLAlchemy(app)


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    clave = db.Column(db.String(50), nullable=False)
    administrador = db.Column(db.Integer, nullable=False, default=0)
    empleado = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, id_usuario, nombre_usuario, clave, administrador, empleado):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.administrador = administrador
        self.empleado = empleado


usuarios_bd = [
    Usuario(1, "Milena", "mile3155", administrador=True, empleado=True),
    Usuario(2, "Mario", "mario123", administrador=False, empleado=True),
    Usuario(3, "JuanCamilo", "juanc789", administrador=False, empleado=True)
]


@login_manager.user_loader
def cargar_usuario(id_usuario):
    for usuario in usuarios_bd:
        if usuario.id_usuario == int(id_usuario):
            return usuario
    return None


# Rutas
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        nombre_usuario = request.form["nombre_usuario"]
        clave = request.form["clave"]

        for usuario in usuarios_bd:
            if usuario.nombre_usuario == nombre_usuario and usuario.clave == clave:
                login_user(Usuario.self)
                flash('Inicio de sesión correcto', 'success')
                if usuario.administrador:
                    return redirect(url_for('administrador'))
                else:
                    return redirect(url_for('ruta'))
            else:
                flash('Credenciales incorrectas, haz un nuevo intento', 'danger')


@app.route('/administrador')
def administrador():
    return render_template("administrador.html")


@app.route('/ruta')
def ruta():
    return render_template("ruta.html")


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


@app.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    try:
        ingredientes = Ingrediente.query.all()
        ingredientes_data = []
        for ingrediente in ingredientes:
            ingredientes_data = {
                'id_ingrediente': ingrediente.id_ingrediente,
                'nombre': ingrediente.nombre,
                'contador': ingrediente.contador,
                'precio': ingrediente.precio,
                'calorias': ingrediente.calorias,
                'vegetariano': ingrediente.vegetariano
                }
        return jsonify({'ingredientes': ingredientes_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080,use_reloader=False)