# main.py

from interfaz import pedir_datos_usuario
from generar_boletos import generar_boletos
from utils import abrir_pdf

def main():
    # Pedir los datos al usuario
    ruta_directorio, letra_serie, numero_serie, num_boletos = pedir_datos_usuario()

    if not ruta_directorio:
        print("Operación cancelada.")
        return

    # Generar los boletos y obtener la ruta del archivo PDF
    archivo_pdf = generar_boletos("Bono Colón C3", letra_serie, numero_serie, num_boletos, ruta_directorio)

    # Abrir el archivo PDF automáticamente
    abrir_pdf(archivo_pdf)

if __name__ == "__main__":
    main()
