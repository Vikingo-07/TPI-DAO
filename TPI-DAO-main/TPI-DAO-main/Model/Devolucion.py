class Devolucion:
    def __init__(self, cod_transaccion, fecha_actual, doc_socio, cod_libro, demora):
        """
        Asociarlo al prestamo?
        :param cod_transaccion: id autoincremental de la bd
        :param fecha_actual:
        :param doc_socio:
        :param cod_libro:
        :param demora: 0 si el libro fue devuelto en tiempo y forma.
        """
        self.cod_transaccion = cod_transaccion,
        self.fecha_actual = fecha_actual,
        self.doc_socio = doc_socio,
        self.cod_libro = cod_libro,
        self.dias_demora = demora
