from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, Toplevel, Entry, Listbox, Button, messagebox



class PrincipalWindow:
    def __init__(self):
        # Creación de la ventana
        self.window = Tk()
        self.bandera = False

        # Configuración de la ventana
        self.window.title("Biblioteca")
        self.window.resizable(False, False)
        self.window.state('zoomed')
        # self.window.iconbitmap("../Files/icono.ico")  # Necesitarás proporcionar la ruta correcta a tu archivo .ico
        self.window.configure(bg="gray22")

        # Menu>Botones
        botonera = ttk.Frame(self.window, padding=(10, 10, 10, 10), style="My.TFrame")
        botonera.config(width=200, height=self.window.winfo_height(), borderwidth=2)
        botonera.pack(side='left', fill='y')

        btn_socios = Button(botonera, text="Socios", bg="medium turquoise", padx="50", pady="50", borderwidth=0,
                            foreground="white", font=("Arial", 10, "bold"), cursor="target")
        btn_socios.winfo_rgb('turquoise')
        btn_socios.pack(side="top", pady=10)
        btn_socios["command"] = self.socios

        btn_libros = Button(botonera, text="Libros", bg="medium turquoise", padx="51", pady="50", borderwidth=0,
                            foreground="white", font=("Arial", 10, "bold"), cursor="target")
        btn_libros.pack(side="top", pady=10)
        btn_libros["command"] = self.libros

        btn_prestamos = Button(botonera, text="Prestamos", bg="medium turquoise", padx="39", pady="50", borderwidth=0,
                               foreground="white", font=("Arial", 10, "bold"), cursor="target")
        btn_prestamos.pack(side="top", pady=10)
        btn_prestamos["command"] = self.prestamos

        btn_extraviados = Button(botonera, text="Libros Extraviados", bg="medium turquoise", padx="19", pady="50",
                                 borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        btn_extraviados.pack(side="top", pady=10)
        btn_extraviados["command"] = self.extraviados

        btn_reportes = Button(botonera, text="Reportes", bg="medium turquoise", padx="44", pady="50", borderwidth=0,
                              foreground="white", font=("Arial", 10, "bold"), cursor="target")
        btn_reportes.pack(side="top", pady=10)
        btn_reportes["command"] = self.reportes

        # ESTILOS
        self.window.style = ttk.Style()
        self.window.style.configure("My.TFrame", background="medium turquoise")

        # Esquema
        self.lblgral = Label(self.window, text="", font=("Arial", 20), bg="gray22", fg="white")
        self.lblgral.pack(side="top", pady=10)

    # VISTAS
    def socios(self):
        self.eliminar_botones_reporte()
        self.eliminar_botones_libros_extraviados()
        self.lblgral.configure(text="Socios")

    def libros(self):
        self.eliminar_botones_reporte()
        self.eliminar_botones_libros_extraviados()
        self.lblgral.configure(text="Libros")

    def prestamos(self):
        self.eliminar_botones_reporte()
        self.eliminar_botones_libros_extraviados()
        self.lblgral.configure(text="Prestamos y devoluciones")

    def extraviados(self):
        self.eliminar_botones_reporte()
        self.eliminar_botones_libros_extraviados()
        self.lblgral.configure(text="Libros extraviados")
        self.crear_boton_extravio()

    def crear_boton_extravio(self):
        if hasattr(self, 'btn_abmExtravio'):
            return
        
        self.btn_abmExtravio = Button(self.window, text="Lista de libros extraviados", bg="CadetBlue4", padx="44",
                                  pady="30", borderwidth=0, foreground="white",
                                  font=("Arial", 10, "bold"), cursor="target")
        self.btn_abmExtravio.pack(side="top", pady=10)
        self.btn_abmExtravio["command"] = self.libros_extraviados_command

    def libros_extraviados_command(self):
        
        window_extravio = Toplevel(self.window)
        window_extravio.title("Registro de Libros Extraviados")
        window_extravio.geometry("+250+100")
        window_extravio.geometry("600x300")
        window_extravio.iconbitmap("../Files/icono.ico")
        window_extravio.configure(bg="gray22")

        label_extravio = Label(window_extravio, text="Registro de Libros Extraviados", font=("Arial", 20), bg="gray22", fg="white")
        label_extravio.pack(pady=10)

        # Configurar la Treeview
        columns = ("Codigo", "Titulo", "Precio de reposicion", "Estado")
        treeview = ttk.Treeview(window_extravio, columns=columns)
        for col in columns:
            treeview.heading(col, text=col, anchor="center")
            treeview.column(col, width=150, anchor="center")
        # Ocultar la primera columna en blanco
        treeview["show"] = "headings"

        treeview.pack(padx=10, pady=10)
        
        
        self.textboxes = []
        for i, col in enumerate(columns[:1]):
            label = Label(window_extravio, text=col, bg="gray22", fg="white")
            label.pack(pady=5)
            entry = Entry(window_extravio)
            entry.pack(pady=5)
            self.textboxes.append(entry)

        def submit():
       
            libro_id = self.textboxes[0].get()  # Suponiendo que el ID está en el primer cuadro de texto
            

        # Llama a la función registrar_extravio con los valores obtenidos
            registrar_extravio(libro_id)

            # Cierra la ventana después de procesar el registro
            window_extravio.destroy()
        submit_button = Button(window_extravio, text="Cambiar estado de libro", command=submit, bg="CadetBlue4", padx="20", pady="10",
                           borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        submit_button.pack(pady=10) 
          
        
    def eliminar_botones_libros_extraviados(self):
        if self.bandera:
            self.bandera = False
            self.btn_abmExtravio.destroy()
            
    def reportes(self):
        self.eliminar_botones_reporte()
        self.eliminar_botones_libros_extraviados()
        self.lblgral.configure(text="Reportes")
        self.crear_botones()

    def crear_botones(self):
        if self.bandera:
            return
        self.bandera = True
        self.btn_reporte_libros_estado = Button(self.window, text="Libros por estado", bg="CadetBlue4", padx="44",
                                                pady="30", borderwidth=0, foreground="white",
                                                font=("Arial", 10, "bold"), cursor="target")
        self.btn_reporte_libros_estado.pack(side="top", pady=5)
        self.btn_reporte_libros_estado["command"] = self.reporte_libros_estado

        self.btn_reporte_suma_libros_extraviados = Button(self.window, text="Costo de libros extraviados",
                                                          bg="CadetBlue4", padx="14", pady="30", borderwidth=0,
                                                          foreground="white", font=("Arial", 10, "bold"),
                                                          cursor="target")
        self.btn_reporte_suma_libros_extraviados.pack(side="top", pady=5)
        self.btn_reporte_suma_libros_extraviados["command"] = self.reporte_suma_libros_extraviados

        self.btn_reporte_solicitante_libro = Button(self.window, text="Solicitantes de Libro", bg="CadetBlue4",
                                                    padx="33", pady="30", borderwidth=0, foreground="white",
                                                    font=("Arial", 10, "bold"), cursor="target")
        self.btn_reporte_solicitante_libro.pack(side="top", pady=5)
        self.btn_reporte_solicitante_libro["command"] = self.reporte_solicitante_libro

        self.btn_reporte_prestamos_socio = Button(self.window, text="Préstamos de Socio", bg="CadetBlue4", padx="36",
                                                  pady="30", borderwidth=0, foreground="white",
                                                  font=("Arial", 10, "bold"), cursor="target")
        self.btn_reporte_prestamos_socio.pack(side="top", pady=5)
        self.btn_reporte_prestamos_socio["command"] = self.reporte_prestamos_socio

        self.btn_reporte_prestamos_demorado = Button(self.window, text="Préstamos demorados", bg="CadetBlue4",
                                                     padx="29", pady="30", borderwidth=0, foreground="white",
                                                     font=("Arial", 10, "bold"), cursor="target")
        self.btn_reporte_prestamos_demorado.pack(side="top", pady=5)
        self.btn_reporte_prestamos_demorado["command"] = self.reporte_prestamos_demorado

    def eliminar_botones_reporte(self):
        if self.bandera:
            self.bandera = False
            self.btn_reporte_libros_estado.destroy()
            self.btn_reporte_suma_libros_extraviados.destroy()
            self.btn_reporte_prestamos_demorado.destroy()
            self.btn_reporte_prestamos_socio.destroy()
            self.btn_reporte_solicitante_libro.destroy()
            

    def reporte_libros_estado(self):
        window_books = Toplevel(self.window)
        window_books.title("Cantidad de Libros por estado")
        window_books.geometry("+250+100")
        window_books.geometry("600x300")
        window_books.iconbitmap("../Files/icono.ico")
        window_books.configure(bg="gray22")

        cant_disp = 2 # modificar
        cant_prest = 3 # modificar
        cant_extrav = 5 # modificar

        label_book = Label(window_books, text="Cantidad de Libros por estado", font=("Arial", 20), bg="gray22",
                            fg="white")
        label_book.pack(pady=10)
        label_book3 = Label(window_books, text=f"Disponibles: {cant_disp}", font=("Arial", 12), bg="gray22", fg="white")
        label_book3.pack(pady=10)
        label_book1 = Label(window_books, text=f"Prestados: {cant_prest}", font=("Arial", 12), bg="gray22", fg="white")
        label_book1.pack(pady=10)
        label_book2 = Label(window_books, text=f"Extraviados: {cant_extrav}", font=("Arial", 12), bg="gray22",
                            fg="white")
        label_book2.pack(pady=10)

        def submit():
            window_books.destroy()

        submit_button = Button(window_books, text="Aceptar", command=submit, bg="CadetBlue4", padx="20", pady="10",
                               borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        submit_button.pack(pady=10)

    def reporte_suma_libros_extraviados(self):
        window_books = Toplevel(self.window)
        window_books.title("Costo por libros extraviados")
        window_books.geometry("+250+100")
        window_books.geometry("600x100")
        window_books.iconbitmap("../Files/icono.ico")
        window_books.configure(bg="gray22")

        cant_disp = 500  # modificar
        label_book = Label(window_books, text=f"El costo total para reponer los libros extraviados es ${cant_disp}.",
                           font=("Arial", 12), bg="gray22", fg="white")
        label_book.pack(pady=10)

        def submit():
            window_books.destroy()

        submit_button = Button(window_books, text="Aceptar", command=submit, bg="CadetBlue4", padx="20", pady="10",
                               borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        submit_button.pack(pady=10)

    def reporte_solicitante_libro(self):
        window_book = Toplevel(self.window)
        window_book.title("Ingrese el titulo del libro para listar sus solicitantes")
        window_book.geometry("+250+100")
        window_book.geometry("600x150")
        window_book.iconbitmap("../Files/icono.ico")
        window_book.configure(bg="gray22")

        label_book = Label(window_book, text="Titulo del libro:", font=("Arial", 20), bg="gray22", fg="white")
        label_book.pack(pady=10)
        title_input = Entry(window_book, font=("Arial", 10, "bold"), width=40, justify="center")
        title_input.pack(pady=10)

        def submit():
            # self.window_book.destroy()
            title_book = title_input.get()
            window_solicitante = Toplevel(self.window)
            window_solicitante.title(f"Solicitantes de {title_book}")
            window_solicitante.geometry("+250+100")
            window_solicitante.geometry("600x400")
            window_solicitante.iconbitmap("../Files/icono.ico")
            window_solicitante.configure(bg="gray22")
            label_solicitantes = Label(window_solicitante, text=f"Solicitantes de {title_book}", font=("Arial", 20),
                                       bg="gray22", fg="white")
            label_solicitantes.pack(pady=10)
            listbox = Listbox(window_solicitante, height=15,
                              width=15,
                              bg="grey",
                              activestyle='dotbox',
                              font="Helvetica",
                              fg="black")
            i = 0
            retorno = ["prueba1", "prueba2", "prueba3"]
            for solcitante in retorno:
                i += 1
                listbox.insert(i, solcitante)
            listbox.pack()

            def submit2():
                window_book.destroy()
                window_solicitante.destroy()

            submit2_button = Button(window_solicitante, text="Aceptar", command=submit2, bg="CadetBlue4", padx="20", pady="10",
                                   borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
            submit2_button.pack(pady=10)


        submit_button = Button(window_book, text="Aceptar", command=submit, bg="CadetBlue4", padx="20", pady="10",
                               borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        submit_button.pack(pady=10)

    def reporte_prestamos_socio(self):
        window_prestamos = Toplevel(self.window)
        window_prestamos.title("Ingrese el número del solicitante para listar sus prestamos")
        window_prestamos.geometry("+250+100")
        window_prestamos.geometry("600x150")
        window_prestamos.iconbitmap("../Files/icono.ico")
        window_prestamos.configure(bg="gray22")

        vcmd = self.window.register(self.validate_number)
        label_book = Label(window_prestamos, text="Número del solicitante:", font=("Arial", 20), bg="gray22", fg="white")
        label_book.pack(pady=10)
        number_input = Entry(window_prestamos, validate="key", validatecommand=(vcmd, "%P", "%S"), font=("Arial", 10, "bold"), width=40, justify="center")
        number_input.pack(pady=10)

        def submit():
            # self.window_book.destroy()
            number = number_input.get()
            socio = "pepito" # modificar
            window_solicitante = Toplevel(self.window)
            window_solicitante.title(f"Solicitantes de {socio}")
            window_solicitante.geometry("+250+100")
            window_solicitante.geometry("600x400")
            window_solicitante.iconbitmap("../Files/icono.ico")
            window_solicitante.configure(bg="gray22")
            label_solicitantes = Label(window_solicitante, text=f"Prestamos de {socio}", font=("Arial", 20),
                                       bg="gray22", fg="white")
            label_solicitantes.pack(pady=10)
            listbox = Listbox(window_solicitante, height=15,
                              width=15,
                              bg="grey",
                              activestyle='dotbox',
                              font="Helvetica",
                              fg="black")
            i = 0
            retorno = ["prueba1", "prueba2", "prueba3"]
            for prestamo in retorno:
                i += 1
                listbox.insert(i, prestamo)
            listbox.pack()

            def submit2():
                window_prestamos.destroy()
                window_solicitante.destroy()

            submit2_button = Button(window_solicitante, text="Aceptar", command=submit2, bg="CadetBlue4", padx="20", pady="10",
                                   borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
            submit2_button.pack(pady=10)

        submit_button = Button(window_prestamos, text="Aceptar", command=submit, bg="CadetBlue4", padx="20", pady="10",
                               borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        submit_button.pack(pady=10)

    def reporte_prestamos_demorado(self):
        window_prestamos = Toplevel(self.window)
        window_prestamos.title("Lista de préstamos demorados")
        window_prestamos.geometry("+250+100")
        window_prestamos.geometry("600x400")
        window_prestamos.iconbitmap("../Files/icono.ico")
        window_prestamos.configure(bg="gray22")

        label_solicitantes = Label(window_prestamos, text="Lista de préstamos demorado", font=("Arial", 20),
                                   bg="gray22", fg="white")
        label_solicitantes.pack(pady=10)
        listbox = Listbox(window_prestamos, height=15,
                          width=15,
                          bg="grey",
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="black")
        i = 0
        retorno = ["prueba1", "prueba2", "prueba3"]
        for prestamo in retorno:
            i += 1
            listbox.insert(i, prestamo)
        listbox.pack()

        def submit():
            window_prestamos.destroy()

        submit2_button = Button(window_prestamos, text="Aceptar", command=submit, bg="CadetBlue4", padx="20",
                                pady="10",
                                borderwidth=0, foreground="white", font=("Arial", 10, "bold"), cursor="target")
        submit2_button.pack(pady=10)

    def validate_number(self, new_value, user_input):
        if new_value.isnumeric() and int(new_value) >= 0:
            return True
        else:
            return False

    def mostrar(self):
        self.window.mainloop()

PrincipalWindow().mostrar()
