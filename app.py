import db.base_datos as sqldb

base_datos= sqldb.BaseDatos(**sqldb.conexion_db)


base_datos.mostrar_db()