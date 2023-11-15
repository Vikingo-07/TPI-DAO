from datetime import datetime, timedelta

import Database.Database
from Database.Database import *
from Model.Libro import Libro
from Model.Socio import Socio


def alta_socio(socio):
    crear_socio(socio.documento, socio.nombre, socio.apellido, socio.telefono)


def mod_socio(socio):
    modificar_socio(socio.id, socio.nombre, socio.apellido, socio.telefono)


def baja_socio(socio_id):
    eliminar_socio(socio_id)


def alta_libro(libro):
    precio_rep = round(libro.precio_rep, 2)
    crear_libro(libro.codigo, libro.titulo, precio_rep, libro.estado)


def mod_libro(libro):
    precio_rep = round(libro.precio_rep, 2)
    modificar_libro(libro.id, libro.titulo, precio_rep, libro.estado)


def baja_libro(libro_id):
    eliminar_libro(libro_id)


def buscar_all_libros():
    libros = get_all_libros()
    all_libros = []
    for libro in libros:
        id_libros, codigo, nombre, precio_rep, estado = libro
        all_libros.append(Libro(id_libros, codigo, nombre, precio_rep, estado))


def buscar_all_socios():
    socios = get_all_socios()
    all_socios = []
    for socio in socios:
        print(socio)
        id_socio, nro_documento, nombre, apellido, telefono = socio
        all_socios.append(Socio(id_socio, nro_documento, nombre, apellido, telefono))
    return all_socios


def registrar_prestamo(prestamo):
    #TODO: validar que el estado del libro sea DISPONIBLE
    fecha_prestamo = datetime.strftime(datetime.today(), "%d/%m/%Y")
    registrar_prestamo(prestamo.libro, prestamo.socio, fecha_prestamo, prestamo.dias_pactados)


def registrar_devolucion(prestamo):
    fecha_devolucion = datetime.strftime(datetime.today(), "%d/%m/%Y")
    demora_dias = datetime.strptime(
        fecha_devolucion, "%d/%m/%Y") - datetime.strptime(
        prestamo.fecha_prestamo, "%d/%m/%Y")
    registrar_devolucion(prestamo.id, fecha_devolucion, demora_dias, prestamo.libro)


def registrar_libro_prestado(cod_libro):
    """
    No utilizar para las devoluciones y los prestamos. Esas funciones ya realizan la actualización por su cuenta.
    :param cod_libro:
    :return:
    """
    actualizar_estado_libro(cod_libro, 'PRESTADO')


def registrar_libro_devuelto(cod_libro):
    """
    No utilizar para las devoluciones y los prestamos. Esas funciones ya realizan la actualización por su cuenta.
    El metodo puede servir para registrar un libro que fue devuelto tiempo despues de registrarse como extraviado.
    :param cod_libro:
    :return:
    """
    actualizar_estado_libro(cod_libro, 'DISPONIBLE')


def registrar_libro_extraviado(cod_libro):
    actualizar_estado_libro(cod_libro, 'EXTRAVIADO')


def verificar_socio_habilitado_prestamo(socio_id):
    cant_prestamos_activos = contar_prestamos_activos(socio_id)
    if cant_prestamos_activos >= 3:
        return False # No esta habilitado porque tiene 3 o mas libros pedidos
    hoy = datetime.now().date()
    prestamos_activos = prestamos_activos_de_socio(socio_id)
    for prestamo_activo in prestamos_activos:
        fecha_pactada = (datetime.strptime(prestamo_activo[0], "%d/%m/%Y") + timedelta(days=prestamo_activo[1])).date()

        if fecha_pactada < hoy:
            return False
    return True


def buscar_socio_por_documento(socio_docu):
    return get_socio_por_documento(socio_docu)


def buscar_socio_por_id(socio_id):
    return get_socio_por_id(socio_id)


def buscar_libro_por_id(libro_id):
    return get_libro_por_id(libro_id)


def buscar_libro_por_titulo(libro_titulo):
    return get_libro_por_titulo(libro_titulo)


def buscar_libro_por_codigo(libro_codigo):
    return get_libro_por_codigo(libro_codigo)

def libros_por_estado(estado):
    """
    Busca libros dado un estado ingresado que puede ser.
    :param estado: DISPONIBLE, PRESTADO, EXTRAVIADO
    :return:
    """
    return get_libros_por_estado(estado)


def get_libros_extraviados():
    """
    El metodo devuelve todos los libros que se encuentran prestados y
    que ya hayan pasado 30 dias de la fecha de devolucion
    :return: lista de Libros
    """
    demoras = get_demoras()
    libros = []
    for demora in demoras:
        libro_id, fecha_prestamo, dias_pactados = demora
        fecha_prestamo = datetime.strptime(fecha_prestamo, "%d/%m/%Y")
        dias_pactados = timedelta(days=(dias_pactados + 30))
        if fecha_prestamo.date() + dias_pactados < datetime.now().date():
            libro_id, codigo, nombre, precio_rep, estado = get_libro_por_id(libro_id)
            libro = Libro(libro_id, codigo, nombre, precio_rep, estado)
            libros.append(libro)
    return libros



# Funciones para reportes

def cantidad_libros_por_estado():
    return Database.Database.cantidad_libros_por_estado()


def total_costo_reposicion():
    return sumatoria_precio_reposicion_libros_extraviados()


def solicitantes_libro(titulo):
    return solicitantes_de_libro(titulo)


def prestamos_socio(socio_id):
    return prestamos_de_socio(socio_id)


def prestamos_demorados():
    hoy = datetime.now().date()

    prestamos = Database.Database.prestamos_demorados()
    prestamosDemorados = []
    for prestamo in prestamos:
        fecha_pactada = (datetime.strptime(prestamo[3], "%d/%m/%Y") + timedelta(days=prestamo[4])).date()

        if fecha_pactada < hoy:
            prestamosDemorados.append(prestamo)
    return prestamosDemorados


print(get_libros_extraviados())