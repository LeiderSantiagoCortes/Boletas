# Generador de Boletos en PDF

Este proyecto es una herramienta para generar boletos personalizados en formato PDF. Permite configurar títulos, números de serie y generar múltiples boletos organizados en formato de cuadrícula. Incluye una interfaz gráfica para la entrada de datos y opciones de confirmación en caso de series duplicadas.

## Características

- **Generación de boletos en PDF**: Crea boletos con título, número de serie y números aleatorios.
- **Organización en cuadrícula**: Distribuye boletos en páginas con un formato claro y profesional.
- **Interfaz gráfica (pop-ups)**: Solicita datos al usuario mediante ventanas emergentes.
- **Comprobación de series duplicadas**: Avisa si existe una serie con el mismo número y letra, y ofrece la opción de reemplazarla.
- **Selección de ubicación para guardar**: Permite elegir dónde se guardarán los archivos generados.
- **Configuración personalizable**: Define cuántos boletos generar y cómo se distribuyen.

## Requisitos

- **Python 3.12.5**
- Dependencias del proyecto:
  - `reportlab`
  - `tkinter` (incluido en Python por defecto)

## Instalación

1. **Clona este repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
