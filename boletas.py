import os
import random
from tkinter import Tk
from tkinter.filedialog import askdirectory
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Función para calcular las dimensiones y posición de un boleto
def calcular_posicion_boleto(i, boletos_por_fila, filas_por_pagina, margen_x, margen_y, ancho_boleto, alto_boleto, alto_pagina):
    columna = i % boletos_por_fila
    fila = (i // boletos_por_fila) % filas_por_pagina
    x = margen_x + columna * ancho_boleto
    y = alto_pagina - margen_y - (fila + 1) * alto_boleto
    return x, y


# Función para dibujar un boleto en el canvas
def dibujar_boleto(c, x, y, ancho_boleto, alto_boleto, titulo, letra_serie, numero_serie, padding, fuente_titulo, fuente_texto, tamano_fuente_titulo, tamano_fuente_texto):
    # Dibujar el borde del boleto
    c.rect(x, y, ancho_boleto, alto_boleto)

    # Dibujar el título y la serie del boleto en la misma línea
    c.setFont(fuente_titulo, tamano_fuente_titulo)
    c.drawString(x + padding, y + alto_boleto - 20, titulo)

    # Desplazar la serie a la derecha del título
    c.setFont(fuente_texto, tamano_fuente_texto)
    c.drawString(x + padding + 100, y + alto_boleto - 20, f"{letra_serie}{numero_serie}")

    # Dibujar los números aleatorios
    numeros = random.sample(range(1000, 10000), 4)  # Números de 4 dígitos
    y_texto = y + alto_boleto - 40
    for numero in numeros:
        c.drawString(x + padding, y_texto, str(numero))
        y_texto -= 15


# Función para generar un archivo PDF con varios boletos
def generar_boletos(titulo, letra_serie, numero_serie, num_boletos, ruta_directorio):
    archivo_pdf = os.path.join(ruta_directorio, f"boletos_{letra_serie}{numero_serie}.pdf")
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    ancho_pagina, alto_pagina = letter

    # Configuración de la cuadrícula
    boletos_por_fila = 3
    filas_por_pagina = 5
    margen_x = 30
    margen_y = 40
    ancho_boleto = (ancho_pagina - 2 * margen_x) / boletos_por_fila
    alto_boleto = (alto_pagina - 2 * margen_y) / filas_por_pagina

    # Configuración de estilos
    padding = 10
    fuente_titulo = "Helvetica-Bold"
    fuente_texto = "Helvetica"
    tamano_fuente_titulo = 12
    tamano_fuente_texto = 10

    # Generar boletos
    for i in range(num_boletos):
        x, y = calcular_posicion_boleto(i, boletos_por_fila, filas_por_pagina, margen_x, margen_y, ancho_boleto, alto_boleto, alto_pagina)
        dibujar_boleto(c, x, y, ancho_boleto, alto_boleto, titulo, letra_serie, numero_serie, padding, fuente_titulo, fuente_texto, tamano_fuente_titulo, tamano_fuente_texto)

        # Cambiar a una nueva página si se completa la cuadrícula actual
        if (i + 1) % (boletos_por_fila * filas_por_pagina) == 0:
            c.showPage()

    # Guardar el archivo PDF
    c.save()

    # Abrir automáticamente el archivo PDF
    abrir_pdf(archivo_pdf)


# Función para abrir el archivo PDF automáticamente
def abrir_pdf(archivo_pdf):
    if os.name == 'posix':  # macOS/Linux
        os.system(f"open {archivo_pdf}")
    elif os.name == 'nt':  # Windows
        os.system(f"start {archivo_pdf}")
    print(f"Boletos generados y abiertos: {archivo_pdf}")


# Función principal para configurar y ejecutar el programa
def main():
    # Ocultar la ventana principal de Tkinter
    Tk().withdraw()

    # Seleccionar directorio donde guardar el PDF
    ruta_directorio = askdirectory(title="Selecciona un directorio para guardar los boletos")
    if not ruta_directorio:
        print("No se seleccionó ningún directorio. Cancelando operación.")
        return

    print(f"Guardando boletos en: {ruta_directorio}")

    # Parámetros personalizables
    titulo = "Bono Colón C3"
    letra_serie = input("Ingrese la letra para la serie (ejemplo: A, B, C): ").strip().upper()
    numero_serie = int(input("Ingrese el número de serie para esta ejecución: "))
    num_boletos = int(input("Ingrese la cantidad de boletos a generar: "))

    # Generar los boletos
    generar_boletos(titulo, letra_serie, numero_serie, num_boletos, ruta_directorio)


if __name__ == "__main__":
    main()
