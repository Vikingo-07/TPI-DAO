import sqlite3

def crear_db():
    try:
        # Conectar a la base de datos (o crearla si no existe)
        with sqlite3.connect('database.sqlite3') as conn:
            cursor = conn.cursor()

            # Crear la tabla Libros
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Libros (
                    ID INT PRIMARY KEY AUTOINCREMENT,
                    Codigo INT,
                    Titulo TEXT,
                    PrecioReposicion REAL,
                    Estado TEXT
                )
            ''')

            # Crear la tabla Socios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Socios (
                    ID INT PRIMARY KEY AUTOINCREMENT,
                    nroDocumento INT,
                    Nombre TEXT,
                    apellido TEXT,
                    telefono INT,
                )
            ''')

            # Crear la tabla Prestamos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Prestamos (
                    ID INT PRIMARY KEY AUTOINCREMENT,
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
