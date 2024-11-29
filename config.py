import mysql.connector


# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# creación del cursor
cursor = conexion.cursor()

# creación de nueva base de datos
try:
    cursor.execute("CREATE DATABASE usuarios_db;")
    print("Se creó correctamente la base de datos.")
except:
    print("Ocurrió un error al crear la base de datos. Inténtelo de nuevo.")

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios_db"
)

# creación del cursor
cursor = conexion.cursor()

# creación de una tabla
try:
    cursor.execute("CREATE TABLE usuarios"
                   "(id_usuario INT NOT NULL AUTO_INCREMENT,"
                   "nombre_usuario VARCHAR (50) NOT NULL,"
                   "clave VARCHAR (50) NOT NULL,"
                   "administrador BOOLEAN NOT NULL,"
                   "PRIMARY KEY (id_usuario));")
    print("Se creó correctamente la tabla usuarios.")
except:
    print("Ocurrió un error al intentar crear la tabla usuarios. Inténtelo de nuevo.")

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios_db"
)

# creación del cursor
cursor = conexion.cursor()

sql = "INSERT INTO usuarios (id_usuario, nombre_usuario, clave, administrador) VALUES (%s, %s, %s, %s)"
val = [
    (1, "Milena", "mile3155", True),
    (2, "Mario", "mario123", False),
    (3, "JuanCamilo", "juanc789", False)
]

cursor.executemany(sql, val)
conexion.commit()
print(cursor.rowcount, "Se ha insertado")

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios_db"
)

# creación del cursor
cursor = conexion.cursor()

# creación de una tabla
try:
    cursor.execute("CREATE TABLE ingredientes"
                   "(id INT NOT NULL AUTO_INCREMENT,"
                   "nombre VARCHAR (32) NOT NULL,"
                   "contador INTEGER NOT NULL,"
                   "precio INTEGER NOT NULL,"
                   "calorias INTEGER NOT NULL,"
                   "vegetariano BOOLEAN,"
                   "PRIMARY KEY (id));")
    print("Se creó correctamente la tabla ingredientes.")
except:
    print("Ocurrió un error al intentar crear la tabla ingredientes. Inténtelo de nuevo.")

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios_db"
)

# creación del cursor
cursor = conexion.cursor()

sql = "INSERT INTO ingredientes (id, nombre, contador, precio, calorias, vegetariano) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    (1, 'Helado de fresa', 5, 1200, 100, False),
    (2, 'Chispas de chocolate', 10, 500, 134, True),
    (3, 'Mani Japones', 10, 900, 200, True),
    (4, 'Helado de mandarina', 5, 1200, 50, False),
    (5, 'Helado de chocolate', 5, 1200, 150, False),
    (6, 'Crema Chantilly', 10, 1200, 200, False)
]

cursor.executemany(sql, val)
conexion.commit()
print(cursor.rowcount, "Se ha insertado")

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios_db"
)

# creación del cursor
cursor = conexion.cursor()

# creación de una tabla
try:
    cursor.execute("CREATE TABLE productos"
                   "(id INT NOT NULL AUTO_INCREMENT,"
                   "nombre VARCHAR (32) NOT NULL,"
                   "precio INTEGER,"
                   "id_ingrediente1 INTEGER,"
                   "id_ingrediente2 INTEGER,"
                   "id_ingrediente3 INTEGER,"
                   "PRIMARY KEY (id),"
                   "FOREIGN KEY (id_ingrediente1) REFERENCES ingredientes(id),"
                   "FOREIGN KEY (id_ingrediente2) REFERENCES ingredientes(id),"
                   "FOREIGN KEY (id_ingrediente3) REFERENCES ingredientes(id)) ENGINE=InnoDB;")
    print("Se creó correctamente la tabla productos.")
except:
    print("Ocurrió un error al intentar crear la tabla productos. Inténtelo de nuevo.")

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios_db"
)

# creación del cursor
cursor = conexion.cursor()

sql = "INSERT INTO productos (id, nombre, precio, id_ingrediente1, id_ingrediente2, id_ingrediente3) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    (1, 'Samurai de fresas', 7500, 1, 2, 3),
    (2, 'Samurai de mandarinas', 5100, 4, 2, 3),
    (3, 'Malteada chocoespacial', 14400, 5, 6, 2),
    (4, 'Cupihelado', 6100, 5, 6, 2)
]

cursor.executemany(sql, val)
conexion.commit()
print(cursor.rowcount, "Se ha insertado")
