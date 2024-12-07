---

# Generador de Boletos en PDF

Este proyecto es una herramienta para generar boletos personalizados en formato PDF. Permite configurar títulos, números de serie, y generar múltiples boletos organizados en formato de cuadrícula. Además, incluye una interfaz gráfica para facilitar la entrada de datos y opciones de confirmación en caso de series duplicadas.

## Características

- **Generación de boletos en PDF**: Crea boletos con título, número de serie y números aleatorios.
- **Organización en cuadrícula**: Distribuye boletos en páginas con un formato claro y profesional.
- **Interfaz gráfica (pop-ups)**: Solicita datos al usuario mediante ventanas emergentes.
- **Comprobación de series duplicadas**: Avisa si existe una serie con el mismo número y letra, y ofrece la opción de reemplazarla.
- **Selección de ubicación para guardar**: Elige dónde se guardarán los archivos generados.
- **Configuración personalizable**: Define cuántos boletos generar y cómo se distribuyen.

## Requisitos

- **Python 3.9 o superior**
- Dependencias del proyecto:
  - `reportlab`
  - `tkinter` (incluido en Python por defecto)

## Instalación

1. **Clona este repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Configura un entorno virtual (opcional pero recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En macOS/Linux
   venv\Scripts\activate      # En Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install reportlab
   ```

4. **Verifica la versión de Python**:
   Asegúrate de estar usando Python 3.12.5:
   ```bash
   python --version
   ```

5. **Ignora archivos innecesarios**:
   Este proyecto ya incluye un archivo `.gitignore` para excluir:
   - `__pycache__/`
   - `build/`
   - `dist/`
   - `venv/`
   - `main.spec`
   - `requirements.txt` (opcional si deseas mantenerlo fuera del repositorio).

## Uso

1. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

2. Completa los datos solicitados en los pop-ups:
   - **Título** del boleto.
   - **Letra y número de serie**.
   - **Cantidad de boletos**.

3. Elige la ubicación donde se guardarán los boletos.

4. Si ya existe una serie con la misma letra y número, el sistema te preguntará si deseas reemplazarla.

5. El archivo PDF se generará y abrirá automáticamente al finalizar.

## Distribución como ejecutable

Para crear un ejecutable que no dependa de Python:

1. Instala PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Genera el ejecutable:
   ```bash
   pyinstaller --onefile main.py
   ```

3. El ejecutable estará disponible en la carpeta `dist/`.

## Estructura del proyecto

```plaintext
├── main.py                  # Archivo principal
├── utils/
│   ├── boleto_generator.py  # Lógica para generar boletos
│   ├── file_utils.py        # Funciones para manejo de archivos
│   ├── gui_utils.py         # Funciones para la interfaz gráfica
├── requirements.txt         # Dependencias del proyecto
├── .gitignore               # Archivos y carpetas ignorados por Git
└── README.md                # Documentación del proyecto
```

## Contribución

1. Realiza un fork del proyecto.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza tus modificaciones y realiza un commit:
   ```bash
   git commit -m "Descripción de los cambios"
   ```
4. Envía tus cambios al repositorio remoto:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Crea un Pull Request en GitHub.
---
