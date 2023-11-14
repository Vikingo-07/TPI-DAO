import sqlite3


def crear(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE SOCIOS ("
                       "nroDocumento INT PRIMARY KEY,"
                       "nombre TEXT,"
                       "apellido TEXT,"
                       "telefono INT"
                       ")")# Algun id_Estado para marcar que es deudor moroso?

        cursor.execute("CREATE TABLE LIBROS ("
                       "codigo INT PRIMARY KEY AUTOINCREMENT,"
                       "isbn INT,"
                       "titulo TEXT,"
                       "precio_reposicion REAL,"
                       "estado TEXT,"
                       "fecha_desde TEXT"
                       ")")
# cod_transac, fecha_actual, doc_socio, cod_libro, dias_devolucion
        cursor.execute("CREATE TABLE PRESTAMOS ("
                       "cod_transac INT PRIMARY KEY AUTOINCREMENT,"
                       "fecha_actual TEXT,"
                       "doc_socio INT,"
                       "cod_libro INT,"
                       "dias_devolucion INT"
                       ")")

        cursor.execute("CREATE TABLE DEVOLUCIONES ("
                       "cod_transac INT PRIMARY KEY AUTOINCREMENT,"
                       "fecha_actual TEXT,"
                       "doc_socio INT,"
                       "cod_libro INT,"
                       "dias_demora INT"
                       ")")
    except sqlite3.Error as error:
        print("Error al crear tablas: ", error)

    finally:
        cursor.close()
        conn.close()
