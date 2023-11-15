import datetime


class Libro:
    def __init__(self, id_libro, codigo, titulo, precio_rep, estado):
        self.id = id_libro
        self.codigo = codigo
        self.titulo = titulo
        self.precio_rep = precio_rep
        self.estado = estado
        self.fecha_desde = datetime.datetime.today().strftime("%d/%m/%Y")



