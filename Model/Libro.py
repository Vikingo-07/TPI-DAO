import datetime


class Libro:
    def __init__(self, id_libro, codigo, titulo, precio_rep):
        self.id = id_libro,
        self.codigo = codigo,
        self.titulo = titulo,
        self.precio_rep = precio_rep,
        self.estado = "DISPONIBLE"
        self.fecha_desde = datetime.datetime.today().strftime("%d/%m/%Y")

    def disponible(self):
        self.estado = "DISPONIBLE"
        self.fecha_desde = datetime.datetime.today().strftime("%d/%m/%Y")

    def prestado(self):
        self.estado = "PRESTADO"
        self.fecha_desde = datetime.datetime.today().strftime("%d/%m/%Y")

    def extraviado(self):
        self.estado = "EXTRAVIADO"
        self.fecha_desde = datetime.datetime.today().strftime("%d/%m/%Y")

    def is_missing(self):
        """
        Mal planteado porque la condicion para registrar el extravío es que el libro tenga
        más de 30 días de demora desde la fecha pactada de devolución, no desde la fecha de prestamo.
        Es mas, quizas no debería ser el libro el que controle esto
        :return:
        """
        fecha_hoy = datetime.datetime.strftime(datetime.datetime.today(), "%d/%m/%Y")
        fecha_desde = datetime.datetime.strptime(self.fecha_desde, "%d/%m/%Y")
        diferencia_dias = fecha_hoy - fecha_desde
        return diferencia_dias.days >= 30


