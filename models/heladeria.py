##Proyecto 3 - Edna Milena Chaparro Perez

from funciones import producto_rentable as producto_rentable

class Heladeria:
    # Constructor
    def __init__(self, nombre: str, productos: list = [], ingredientes: list = []) -> None:
        self.nombre = nombre
        self.productos = productos
        self.ingredientes = ingredientes

    # Metodos
    @staticmethod
    def producto_rentable() -> str:
        return producto_rentable()

    def vender_producto(self, producto, nombre, precio):
        if producto in self.productos and self.productos[producto] >= len(self.__productos):
            venta = {
                'producto': producto,
                'cantidad': len(self.__productos),
                'nombre': nombre,
                'precio': precio,
            }
            self.productos.append(venta)
            self.productos[producto] -= len(self.__productos)
            print(f"Venta realizada: {len(self.__productos)} unidades de {producto}")
        else:
            print(f"No hay suficientes unidades de {producto} en el inventario.")

    def mostrar_ventas(self):
        print("\nRegistro de ventas:")
        for venta in self.productos:
            print(
                f"Producto: {venta['producto']} - Cantidad: {venta['cantidad']} - Precio: {venta['precio']}")