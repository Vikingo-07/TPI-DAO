from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import subprocess
import os

current_directory = current_dir = os.path.abspath(os.path.dirname(__file__))
files_directory = os.path.join(current_directory, "../Files/Outputs")
def pdf_libros_estados(cantidades):
    # Crear un documento PDF
    pdf_file_path = os.path.join(files_directory, "cantLibrosXEstado.pdf")
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    # Crear una lista para almacenar los elementos del informe
    elements = []
    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = "Cantidad de libros por estado"
    elements.append(Paragraph(title, styles['Title']))
    # Agregar una tabla de ejemplo
    data = [["Estado", "Cantidad de libros"]]
    for status, quantity in cantidades:
        data.append([status, quantity])

    table = Table(data, colWidths=[1 * inch, 2 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    # Agregar un párrafo de texto
    text = "Este es un informe de cantidad de Libros por estado."
    elements.append(Paragraph(text, styles['Normal']))
    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)
    abrir_pdf(pdf_file_path)

def pdf_gasto_extraviados(cant):
    # Crear un documento PDF
    pdf_file_path = os.path.join(files_directory, "gastoLibrosExtraviados.pdf")
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    # Crear una lista para almacenar los elementos del informe
    elements = []
    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = "Costo total para reponer los libros extraviados"
    elements.append(Paragraph(title, styles['Title']))
    # Agregar una tabla de ejemplo
    data = [["Costo total", f"${cant}"]]

    table = Table(data, colWidths=[2 * inch, 2 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    # Agregar un párrafo de texto
    text = "Este es un informe del costo total para reponer los libros extraviados."
    elements.append(Paragraph(text, styles['Normal']))
    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)
    abrir_pdf(pdf_file_path)


def pdf_solicitantes_libro(solicitantes, busqueda):
    # Crear un documento PDF
    pdf_file_path = os.path.join(files_directory, f"solicitantesLibro-{busqueda}.pdf")
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    # Crear una lista para almacenar los elementos del informe
    elements = []
    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = "Solicitantes por Libro"
    elements.append(Paragraph(title, styles['Title']))
    # Agregar un párrafo de texto
    text = f"Solicitantes de libros que contienen '{busqueda}'"
    elements.append(Paragraph(text, styles['Normal']))
    # Agregar una tabla de ejemplo
    data = [["Libro", "Solicitante"]]
    for solcitante in solicitantes:
        data.append([solcitante[0], f"{solcitante[1]} {solcitante[2]}"])

    table = Table(data, colWidths=[3 * inch, 2 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)
    abrir_pdf(pdf_file_path)

def pdf_prestamos_socio(prestamos, socio):
    # Crear un documento PDF
    pdf_file_path = os.path.join(files_directory, f"prestamosXSocio-{socio[2]}-{socio[3]}.pdf")
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    # Crear una lista para almacenar los elementos del informe
    elements = []
    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = f"Préstamos de {socio[2]} {socio[3]}:"
    elements.append(Paragraph(title, styles['Title']))
    # Agregar una tabla de ejemplo
    data = [["Libro", "Fecha", "Dias pactados"]]
    for prestamo in prestamos:
        data.append(list(prestamo))

    table = Table(data, colWidths=[3 * inch, 2 * inch, 2 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    # Agregar un párrafo de texto
    text = f"Se muestran los {len(prestamos)} préstamos que tiene {socio[2]} {socio[3]}."
    elements.append(Paragraph(text, styles['Normal']))
    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)
    abrir_pdf(pdf_file_path)

def pdf_prestamos_demorados(prestamos):
    # Crear un documento PDF
    pdf_file_path = os.path.join(files_directory, "prestamosDemorados.pdf")
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    # Crear una lista para almacenar los elementos del informe
    elements = []
    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = "Préstamos demorados"
    elements.append(Paragraph(title, styles['Title']))
    # Agregar una tabla de ejemplo
    data = [["Socio", "Libro", "Fecha", "Dias pactados"]]
    for prestamo in prestamos:
        data.append([f"{prestamo[0]} {prestamo[1]}", prestamo[2], prestamo[3], prestamo[4]])

    table = Table(data, colWidths=[2 * inch, 3 * inch, 1 * inch, 2 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    # Agregar un párrafo de texto
    text = "Se muestran todos los préstamos demorados."
    elements.append(Paragraph(text, styles['Normal']))
    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)
    abrir_pdf(pdf_file_path)

def abrir_pdf(pdf_path):
    try:
        subprocess.Popen(["start", "", str(pdf_path)], shell=True)
    except Exception as e:
        print(f"No se pudo abrir el PDF automáticamente: {e}")