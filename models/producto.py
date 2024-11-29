##Proyecto 3 - Edna Milena Chaparro Perez

from funciones import contar_calorias_producto as contar_calorias_producto
from funciones import calcular_costo as calcular_costo
from funciones import calcular_rentabilidad as calcular_rentabilidad
from db import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    # Methods
    def contar_calorias_producto() -> float:
        return contar_calorias_producto()

    def calcular_costo() -> int:
        return calcular_costo()

    def calcular_rentabilidad() -> int:
        return calcular_rentabilidad()
