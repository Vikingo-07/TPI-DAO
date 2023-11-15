from datetime import datetime
import random
import sqlite3
from datetime import timedelta, date


def crear_db():
    try:
        # Conectar a la base de datos (o crearla si no existe)
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()

            # Crear la tabla Libros
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Libros (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Codigo INT,
                    Titulo TEXT,
                    PrecioReposicion REAL,
                    Estado TEXT
                )
            ''')

            # Crear la tabla Socios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Socios (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    nroDocumento INT,
                    Nombre TEXT,
                    apellido TEXT,
                    telefono INT
                )
            ''')

            # Crear la tabla Prestamos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Prestamos (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    LibroId INT,
                    SocioId INT,
                    FechaPrestamo DATE,
                    DiasPactados INT,
                    FechaDevolucion DATE,
                    DemoraDias INT,
                    FOREIGN KEY (LibroId) REFERENCES Libros(ID),
                    FOREIGN KEY (SocioId) REFERENCES Socios(ID)
                )
            ''')

    except sqlite3.Error as error:
        print("Error al crear la base de datos:", error)


def cargar_datos():
    # Arrays con nombres de libros y socios
    nombres_libros = ["Cien años de soledad", "To Kill a Mockingbird", "1984", "The Great Gatsby", "Moby-Dick",
                      "Pride and Prejudice", "The Catcher in the Rye", "One Hundred Years of Solitude",
                      "Brave New World", "The Lord of the Rings", "The Hobbit", "The Da Vinci Code", "The Alchemist",
                      "Harry Potter and the Sorcerer's Stone", "The Hunger Games", "The Kite Runner",
                      "The Fault in Our Stars", "The Shining", "The Girl with the Dragon Tattoo",
                      "The Mystery of Solitaire"]

    nombres_socios = ["John Smith", "Jane Doe", "Robert Johnson", "Emily White", "David Brown", "Linda Miller",
                      "Michael Davis", "Karen Wilson", "William Taylor", "Megan Moore", "Christopher Lee",
                      "Amanda Johnson", "Brian Davis", "Olivia White", "Daniel Wilson", "Eva Taylor", "Mark Miller",
                      "Sophia Moore", "Kevin Anderson", "Chloe Harris"]
    try:
        # Conectar a la base de datos
        with sqlite3.connect('database.sqlite3') as conexion:
            cursor = conexion.cursor()

            # Generar 20 entradas de prueba para la tabla Libros
            for _ in range(20):
                cursor.execute('''
                        INSERT INTO Libros (Codigo, Titulo, PrecioReposicion, Estado)
                        VALUES (?, ?, ?, ?)
                    ''', (random.randint(100, 999), nombres_libros[_], random.uniform(10.0, 50.0),
                          random.choice(['disponible', 'prestado', 'extraviado'])))

            # Generar 20 entradas de prueba para la tabla Socios
            for _ in range(20):
                cursor.execute('''
                        INSERT INTO Socios (nroDocumento, Nombre, Apellido, Telefono)
                        VALUES (?, ?, ?, ?)
                    ''', (random.randint(10000000, 99999999), nombres_socios[_].split()[0],
                          nombres_socios[_][1], random.randint(100000000, 999999999)))

            # Generar 20 entradas de prueba para la tabla Prestamos
            for _ in range(20):
                fecha_prestamo = date.today() - timedelta(days=random.randint(1, 365))
                dias_pactados = timedelta(days=random.randint(1, 25))
                fecha_devolucion = fecha_prestamo + dias_pactados + timedelta(days=random.randint(0, 10))
                cursor.execute('''
                        INSERT INTO Prestamos (LibroId, SocioId, FechaPrestamo, DiasPactados, FechaDevolucion, DemoraDias)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                    random.randint(1, 20), random.randint(1, 20), fecha_prestamo, str(dias_pactados),
                    str(fecha_devolucion),
                    0))

    except sqlite3.Error as error:
        print("Error al cargar datos en la base de datos:", error)


def crear_libro(codigo, titulo, precio_reposicion, estado):
    """

    :param codigo:
    :param titulo:
    :param precio_reposicion:
    :param estado:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Libros (Codigo, Titulo, PrecioReposicion, Estado) VALUES (?, ?, ?, ?)',
                           (codigo, titulo, precio_reposicion, estado))
            conn.commit()
            print("Libro creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el libro: {e}")


def modificar_libro(libro_id, nuevo_titulo, nuevo_precio, nuevo_estado):
    """

    :param libro_id:
    :param nuevo_titulo:
    :param nuevo_precio:
    :param nuevo_estado:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Libros SET Titulo=?, PrecioReposicion=?, Estado=? WHERE ID=?',
                           (nuevo_titulo, nuevo_precio, nuevo_estado, libro_id))
            conn.commit()
            print("Libro modificado exitosamente.")
    except Exception as e:
        print(f"Error al modificar el libro: {e}")


def eliminar_libro(libro_id):
    """

    :param libro_id:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Libros WHERE ID=?', (libro_id,))
            conn.commit()
            print("Libro eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar el libro: {e}")


def get_libro_por_id(libro_id):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Libros WHERE ID = ?', (libro_id,))
            libro = cursor.fetchone()
            return libro
    except Exception as e:
        print(f"Error al buscar libro por ID: {e}")
        return None


def get_libro_por_titulo(libro_titulo):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Libros WHERE Titulo LIKE ?', ('%' + libro_titulo + '%',))
            libros = cursor.fetchall()
            return libros
    except Exception as e:
        print(f"Error al buscar libros por título: {e}")
        return None


def get_libro_por_codigo(libro_codigo):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Libros WHERE Codigo = ?', (libro_codigo,))
            libro = cursor.fetchone()
            return libro
    except Exception as e:
        print(f"Error al buscar libro por código: {e}")
        return None


def crear_socio(documento, nombre, apellido, telefono):
    """

    :param documento:
    :param nombre:
    :param apellido:
    :param telefono:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Socios (nroDocumento, Nombre, apellido, telefono) VALUES (?, ?, ?, ?)',
                           (documento, nombre, apellido, telefono))
            conn.commit()
            print("Socio creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el socio: {e}")


def modificar_socio(socio_id, nuevo_nombre, nuevo_apellido, nuevo_telefono):
    """

    :param socio_id:
    :param nuevo_nombre:
    :param nuevo_apellido:
    :param nuevo_telefono:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Socios SET Nombre=?, apellido=?, telefono=? WHERE ID=?',
                           (nuevo_nombre, nuevo_apellido, nuevo_telefono, socio_id))
            conn.commit()
            print("Socio modificado exitosamente.")
    except Exception as e:
        print(f"Error al modificar el socio: {e}")


def eliminar_socio(socio_id):
    """

    :param socio_id:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Socios WHERE ID=?', (socio_id,))
            conn.commit()
            print("Socio eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar el socio: {e}")


def get_socio_por_documento(socio_docu):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Socios WHERE nroDocumento = ?', (socio_docu,))
            socio = cursor.fetchone()
            return socio
    except Exception as e:
        print(f"Error al buscar socio por documento: {e}")
        return None


def get_socio_por_id(socio_id):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Socios WHERE ID = ?', (socio_id,))
            socio = cursor.fetchone()
            return socio
    except Exception as e:
        print(f"Error al buscar socio por ID: {e}")
        return None


def registrar_prestamo(libro_id, socio_id, fecha_prestamo, dias_pactados):
    """

    :param libro_id:
    :param socio_id:
    :param fecha_prestamo:
    :param dias_pactados:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Prestamos (LibroId, SocioId, FechaPrestamo, DiasPactados) '
                           'VALUES (?, ?, ?, ?, ?)', (libro_id, socio_id, fecha_prestamo, dias_pactados))
            cursor.execute('UPDATE Libros SET Estado=? WHERE ID=?', ('PRESTADO', libro_id))
            conn.commit()
            print("Préstamo registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el préstamo: {e}")


def registrar_devolucion(prestamo_id, fecha_devolucion, demora_dias, libro_id):
    """

    :param libro_id:
    :param prestamo_id:
    :param fecha_devolucion:
    :param demora_dias:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Prestamos SET FechaDevolucion=?, DemoraDias=? WHERE ID=?',
                           (fecha_devolucion, demora_dias, prestamo_id))
            cursor.execute('UPDATE Libros SET Estado=? WHERE ID=?', ('DISPONIBLE', libro_id))

            conn.commit()
            print("Devolución registrada exitosamente.")
    except Exception as e:
        print(f"Error al registrar la devolución: {e}")


def actualizar_estado_libro(libro_id, estado):
    """

    :param libro_id:
    :param estado:
    :return:
    """
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Libros SET Estado=? WHERE ID=?', (estado, libro_id))
            conn.commit()
            print("Libro marcado como EXTRAVIADO exitosamente.")
    except Exception as e:
        print(f"Error al marcar el libro como EXTRAVIADO: {e}")


def obtener_libros_por_estado(estado):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Libros WHERE Estado=?', (estado,))
            libros = cursor.fetchall()
            return libros
    except Exception as e:
        print(f"Error al obtener libros por estado: {e}")
        return None


def obtener_prestamos_por_socio(socio_id):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Prestamos WHERE SocioId=?', (socio_id,))
            prestamos = cursor.fetchall()
            return prestamos
    except Exception as e:
        print(f"Error al obtener préstamos por socio: {e}")
        return None


def obtener_libros_extraviados():
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Libros WHERE Estado=?', ('EXTRAVIADO',))
            libros_extraviados = cursor.fetchall()
            return libros_extraviados
    except Exception as e:
        print(f"Error al obtener libros extraviados: {e}")
        return None


def obtener_prestamos_vencidos():
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            hoy = datetime.now().date()
            cursor.execute('SELECT * FROM Prestamos WHERE FechaDevolucion < ? AND DemoraDias IS NULL', (hoy,))
            prestamos_vencidos = cursor.fetchall()
            return prestamos_vencidos
    except Exception as e:
        print(f"Error al obtener préstamos vencidos: {e}")
        return None


def prestamos_activos_de_socio(socio_id):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()

            # Verificar si algún préstamo activo tiene demora en su devolución
            cursor.execute('SELECT FechaPrestamo, DiasPactados FROM Prestamos WHERE SocioId=? AND FechaDevolucion IS '
                           'NULL', (socio_id,))
            cantidad_devoluciones_demoradas = cursor.fetchall()

            return cantidad_devoluciones_demoradas

    except Exception as e:
        print(f"Error al verificar préstamos activos del socio: {e}")
        return False


def contar_prestamos_activos(socio_id):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM Prestamos WHERE SocioId=? AND FechaDevolucion IS NULL', (socio_id,))
            return cursor.fetchone()[0]
    except Exception as e:
        print(f"Error al contar libros prestados al socio: {e}")
        return None


def get_all_titulos():
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Titulo FROM Libros')
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Error al obtener los titulos de todos los libros: {e}")
        return None


# Metodos para reportes
def cantidad_libros_por_estado():
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Estado, COUNT(*) FROM Libros GROUP BY Estado')
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Error al obtener la cantidad de libros por estado: {e}")
        return None


def sumatoria_precio_reposicion_libros_extraviados():
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SUM(PrecioReposicion) FROM Libros WHERE Estado=?', ('EXTRAVIADO',))
            suma_precio_reposicion = cursor.fetchone()[0]
            return suma_precio_reposicion if suma_precio_reposicion is not None else 0
    except Exception as e:
        print(f"Error al obtener la sumatoria del precio de reposición de libros extraviados: {e}")
        return None


def solicitantes_de_libro(titulo_libro):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Socios.Nombre, Socios.apellido '
                           'FROM Socios '
                           'JOIN Prestamos ON Socios.ID = Prestamos.SocioId '
                           'JOIN Libros ON Prestamos.LibroId = Libros.ID '
                           'WHERE Libros.Titulo LIKE ?', ('%' + titulo_libro + '%',))
            solicitantes = cursor.fetchall()
            return solicitantes
    except Exception as e:
        print(f"Error al obtener los solicitantes del libro: {e}")
        return None


def prestamos_de_socio(socio_id):
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT Libros.Titulo, Prestamos.FechaPrestamo, Prestamos.DiasPactados, Prestamos.FechaDevolucion, '
                'Prestamos.DemoraDias'
                'FROM Prestamos '
                'JOIN Libros ON Prestamos.LibroId = Libros.ID '
                'JOIN Socios ON Prestamos.SocioId = Socios.ID '
                'WHERE Socios.ID = ?', (socio_id,))
            prestamos = cursor.fetchall()
            return prestamos
    except Exception as e:
        print(f"Error al obtener los préstamos del socio: {e}")
        return None


def prestamos_demorados():
    try:
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT Socios.Nombre, Socios.apellido, Libros.Titulo, Prestamos.FechaPrestamo, Prestamos.DiasPactados '
                'FROM Prestamos '
                'JOIN Libros ON Prestamos.LibroId = Libros.ID '
                'JOIN Socios ON Prestamos.SocioId = Socios.ID '
                'WHERE Prestamos.FechaDevolucion is NULL')
            demoras = cursor.fetchall()
            return demoras
    except Exception as e:
        print(f"Error al obtener los préstamos demorados: {e}")
        return None
