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


def mod_libro(libro_id, nuevo_estado):
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

def registrar_extravio(cod_libro):
    # 1. busco en la bd el libro que tengo que modificar
    # 2. Actualizo el estado por extraviado
    #

def main():
    print("Bienvenido al sistema de biblioteca")
    print("1. Alta socio")
    print("2. Mod. Socio")
    print("3. Baja socio")
    print("4. Alta de libros")
    print("5. Mod. de libros")
    print("6. Baja de libros")
    print("7. Registración de préstamos")
    print("8. Registración de devoluciones")
    print("9. Registración de libros extraviados")
    print("10. Reportes")
    print("11. Salir")
    while True:
        opcion = input("Selecciona una opción (1-11): ")

        if opcion == "1":
            alta_socio()
        elif opcion == "2":
            mod_socio()
        elif opcion == "3":
            baja_socio()
        elif opcion == "4":
            alta_libro()
        elif opcion == "5":
            mod_libro()
        elif opcion == "6":
            baja_libro()
        elif opcion == "7":
            registrar_prestamo()
        elif opcion == "8":
            registrar_devolucion()
        elif opcion == "9":
            registrar_extravio()
        elif opcion == "10":
            print("Ops, funcionalidad en desarrollo...")
        elif opcion == "11":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")