##Proyecto 3 - Edna Milena Chaparro Perez

import unittest

from models.funciones import es_sano as es_sano
from models.funciones import contar_calorias_producto as contar_calorias_producto
from models.funciones import calcular_costo as calcular_costo
from models.funciones import calcular_rentabilidad as calcular_rentabilidad
from models.funciones import producto_rentable as producto_rentable


class TestFunciones(unittest.TestCase):
    def test_es_sano(self):
        es_sano(200, True)
        self.assertEqual(es_sano(), True)

    def test_contar_calorias(self):
        contar_calorias_producto([1, 3, 5, 7, 9])
        self.assertEqual(contar_calorias_producto(), 23.75)

    def test_calcular_costo(self):
        calcular_costo(ingredientes=[
            {"nombre": "Helado de fresa", "precio": 1200},
            {"nombre": "Chispas de chocolate", "precio": 500},
            {"nombre": "Mani Japones", "precio": 900}
        ])
        self.assertEqual(calcular_costo(), 2600)

    def test_calcular_rentabilidad(self):
        calcular_rentabilidad(7500, ingredientes=[
            {"nombre": "Helado de fresa", "precio": 1200},
            {"nombre": "Chispas de chocolate", "precio": 500},
            {"nombre": "Mani Japones", "precio": 900}
        ])
        self.assertEqual(calcular_rentabilidad(), 4900)

    def test_producto_rentable(self):
        producto_rentable(productos=[
            {"nombre": "Samurai de fresas", "rentabilidad": 4900},
            {"nombre": "Samurai de mandarinas", "rentabilidad": 2500},
            {"nombre": "Malteada chocoespacial", "rentabilidad": 11000},
            {"nombre": "Cupihelado", "rentabilidad": 3200}
        ])
        self.assertEqual(producto_rentable(), "Malteada chocoespacial")


if __name__ == '__main__':
    unittest.main()
