# interfaz.py

from tkinter import Tk, simpledialog, messagebox
from tkinter.filedialog import askdirectory
import os

# Función para pedir datos al usuario a través de popups
def pedir_datos_usuario():
    # Inicializar Tkinter
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Solicitar directorio donde guardar el PDF
    ruta_directorio = askdirectory(title="Selecciona un directorio para guardar los boletos")
    if not ruta_directorio:
        return None, None, None, None

    # Solicitar parámetros de entrada a través de popups
    letra_serie = simpledialog.askstring("Entrada", "Ingrese la letra para la serie (ejemplo: A, B, C):")
    if not letra_serie:
        return None, None, None, None

    try:
        numero_serie = int(simpledialog.askstring("Entrada", "Ingrese el número de serie para esta ejecución:"))
    except ValueError:
        return None, None, None, None

    try:
        num_boletos = int(simpledialog.askstring("Entrada", "Ingrese la cantidad de boletos a generar:"))
    except ValueError:
        return None, None, None, None

    # Verificar si ya existe un archivo con esa serie
    archivo_pdf = os.path.join(ruta_directorio, f"boletos_{letra_serie}{numero_serie}.pdf")
    if os.path.exists(archivo_pdf):
        respuesta = messagebox.askyesno(
            "Archivo ya existe",
            f"Ya existe un archivo con la serie {letra_serie}{numero_serie}. ¿Deseas reemplazarlo?"
        )
        if not respuesta:  # Si la respuesta es No
            return pedir_datos_usuario()  # Volver a pedir los datos

    return ruta_directorio, letra_serie.upper(), numero_serie, num_boletos
