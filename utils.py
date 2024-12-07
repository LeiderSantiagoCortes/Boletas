
import os

# Función para abrir el archivo PDF automáticamente
def abrir_pdf(archivo_pdf):
    if os.name == 'posix':  # macOS/Linux
        os.system(f"open {archivo_pdf}")
    elif os.name == 'nt':  # Windows
        os.system(f"start {archivo_pdf}")
    print(f"Boletos generados y abiertos: {archivo_pdf}")
