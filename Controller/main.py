import sqlite3

from Model import *

dbFile = "database.sqlite3"


# Administracion de socios
def alta_socio(socio):
    try:
        with sqlite3.connect(dbFile) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO SOCIOS (nroDocumento, nombre, apellido, telefono) VALUES (?, ?, ?, ?)",
                (socio.nroDocumento, socio.nombre, socio.apellido, socio.telefono))

            # Confirmar la transacción
            conn.commit()

    except sqlite3.Error as error:
        print("Error al registrar al socio: ", error)


def mod_socio():
    pass


def baja_socio():
    pass


# Admin. de Libros

def alta_libro(libro):
    try:
        with sqlite3.connect(dbFile) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO LIBROS (isbn, titulo, precio_reposicion, estado, fecha_desde) VALUES (?, ?, ?, ?, ?)",
                (libro.isbn, libro.titulo, libro.precio_rep, libro.estado, libro.fecha_desde))

            # Confirmar la transacción
            conn.commit()

    except sqlite3.Error as error:
        print("Error al registrar al socio: ", error)


def mod_libro():
    pass


def baja_libro():
    pass


def registrar_prestamo(prestamo):
    try:
        with sqlite3.connect(dbFile) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO PRESTAMOS (fecha_actual, doc_socio, cod_libro, dias_devolucion) VALUES (?, ?, ?, ?)",
                (prestamo.fecha_actual, prestamo.doc_socio, prestamo.cod_libro, prestamo.dias_devolucion))

            # Confirmar la transacción
            conn.commit()

    except sqlite3.Error as error:
        print("Error al registrar prestamo: ", error)


def registrar_devolucion(devolucion):
    try:
        with sqlite3.connect(dbFile) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO DEVOLUCIONES (fecha_actual, doc_socio, cod_libro, dias_demora) VALUES (?, ?, ?, ?)",
                (devolucion.fecha_actual, devolucion.doc_socio, devolucion.cod_libro, devolucion.dias_demora))

            # Confirmar la transacción
            conn.commit()

    except sqlite3.Error as error:
        print("Error al registrar devolucion: ", error)
