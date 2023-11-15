class Prestamo:
    def __init__(self, id_prestamo, cod_libro, doc_socio, fecha_prestamo, dias_pactados):
        self.id = id_prestamo
        self.libro = cod_libro
        self.socio = doc_socio
        self.fecha_prestamo = fecha_prestamo
        self.dias_pactados = dias_pactados
        self.fecha_devolucion = None
        self.demora_dias = 0
