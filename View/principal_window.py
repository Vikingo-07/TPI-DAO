from tkinter import *
from tkinter import ttk


class PrincipalWindow:
    def __init__(self):
        # Creación de la ventana
        self.window = Tk()

        # Configuración de la ventana
        self.window.title("Biblioteca")
        self.window.resizable(False, False)
        self.window.state('zoomed')
        self.window.iconbitmap("../Files/icono.ico")
        self.window.configure(bg="gray22")

        # Creación y ubicación de los botones
        botonera = ttk.Frame(self.window, padding=(10, 10, 10, 10), style="My.TFrame")
        botonera.config(width=200, height=self.window.winfo_height(), borderwidth=2)
        botonera.pack(side='left', fill='y')

        btn_socios = Button(botonera, text="Socios", bg="medium turquoise", padx="50", pady="20", borderwidth=0, foreground="white", font=("Arial", 10, "bold"))
        btn_socios.winfo_rgb('turquoise')
        btn_socios.pack(side="top", pady=10)
        btn_socios["command"] = self.socios

        btn_libros = Button(botonera, text="Libros", bg="medium turquoise", padx="51", pady="20", borderwidth=0, foreground="white", font=("Arial", 10, "bold"))
        btn_libros.pack(side="top", pady=10)
        btn_libros["command"] = self.libros

        btn_prestamos = Button(botonera, text="Prestamos", bg="medium turquoise", padx="39", pady="20", borderwidth=0, foreground="white", font=("Arial", 10, "bold"))
        btn_prestamos.pack(side="top", pady=10)
        btn_prestamos["command"] = self.prestamos

        btn_extraviados = Button(botonera, text="Libros Extraviados", bg="medium turquoise", padx="19", pady="20", borderwidth=0, foreground="white", font=("Arial", 10, "bold"))
        btn_extraviados.pack(side="top", pady=10)
        btn_extraviados["command"] = self.extraviados

        btn_reportes = Button(botonera, text="Reportes", bg="medium turquoise", padx="44", pady="20", borderwidth=0, foreground="white", font=("Arial", 10, "bold"))
        btn_reportes.pack(side="top", pady=10)
        btn_reportes["command"] = self.reportes


        #ESTILOS
        self.window.style = ttk.Style()
        self.window.style.configure("My.TFrame", background="medium turquoise")

        # Esquema
        self.lblgral = Label(self.window, text="", font=("Arial", 20), bg="gray22", fg="white")
        self.lblgral.pack(side="top", pady=10)


    # VISTAS
    def socios(self):
        self.lblgral.configure(text="Socios")

    def libros(self):
        self.lblgral.configure(text="Libros")

    def prestamos(self):
        self.lblgral.configure(text="Prestamos y devoluciones")

    def extraviados(self):
        self.lblgral.configure(text="Libros extraviados")

    def reportes(self):
        self.lblgral.configure(text="Reportes")

    def mostrar(self):
        self.window.mainloop()


PrincipalWindow().mostrar()
