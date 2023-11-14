class Prestamo:
    def __init__(self, cod_transaccion, fecha_actual, doc_socio, cod_libro, devolucion):
        """
        Hacer un prestamo y un detalle_prestamo? Tiene sentido si en un prestamo puede sacar mas de un libro.
        Hay alguna otra situacion para la que tenga sentido?
        :param cod_transaccion: id autoincremental de la bd
        :param fecha_actual:
        :param doc_socio:
        :param cod_libro:
        :param devolucion:
        """
        self.cod_transaccion = cod_transaccion,
        self.fecha_actual = fecha_actual,
        self.doc_socio = doc_socio,
        self.cod_libro = cod_libro,
        self.demora = devolucion
