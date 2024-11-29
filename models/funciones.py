##Proyecto 3 - Edna Milena Chaparro Perez

##1 esto es sano
def es_sano(calorias: int, vegetariano: bool) -> bool:
    if calorias>100 and vegetariano:
        return True
    else:
        return False

##2 calorias
def contar_calorias_producto(listaCalorias) -> float:
    suma = 0
    for i in listaCalorias:
        suma = suma + i
    return (round((suma*0.95),2))

##3 costos
def calcular_costo(ingredientes = []) -> int:
    for i in ingredientes:
        resumen = {ingredientes[i]["nombre"]:ingredientes[i]["precio"] for i in range(len(ingredientes)) }
        return sum(resumen.values())

##4 rentabilidad
def calcular_rentabilidad(precio:int, ingredientes = [])  -> int:
    for i in ingredientes:
        resumen = {ingredientes[i]["nombre"]:ingredientes[i]["precio"] for i in range(len(ingredientes)) }
        return precio-sum(resumen.values())

##5 mejor producto
def producto_rentable(productos = [])  -> str:
    for i in productos:
        maximo = max(productos, key=lambda d: d["rentabilidad"])
        return maximo["nombre"]