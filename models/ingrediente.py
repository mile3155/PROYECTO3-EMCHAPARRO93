##Proyecto 3 - Edna Milena Chaparro Perez

from funciones import es_sano as es_sano
from db import db

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    contador = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    vegetariano = db.Column(db.Bool, nullable=False)

    # Methods
    @classmethod
    def es_sano() -> bool:
        return es_sano()

    def abastecer(self, nombre, contador, precio, calorias, vegetariano) -> None:
        if nombre in self._inventario:
            self._inventario += contador
        else:
            self._inventario = {
                'cantidad': contador,
                'precio': precio,
                'calorias': calorias,
                'vegetariano': vegetariano
            }

    def mostrar_inventario(self):
        return self.nombre + str(self.contador) + "($" + str(self.precio) + ")"
