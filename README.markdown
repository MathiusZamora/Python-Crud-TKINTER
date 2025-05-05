# Aplicación CRUD para Farmacia

Esta es una aplicación de escritorio desarrollada con Python y Tkinter para gestionar una base de datos de farmacia. Ofrece una interfaz gráfica de usuario (GUI) para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre tres entidades: **Laboratorios**, **Proveedores** y **Artículos**. La aplicación se conecta a una base de datos MySQL para almacenar y recuperar datos.

## Características
- **Gestión de Laboratorios**: Agregar, modificar, eliminar y visualizar registros de laboratorios (nombre, dirección, teléfono, correo, estado).
- **Gestión de Proveedores**: Agregar, modificar, eliminar y visualizar registros de proveedores (nombre, dirección, teléfono, correo, estado).
- **Gestión de Artículos**: Agregar, modificar, eliminar y visualizar registros de artículos (nombre, ID de laboratorio, ID de proveedor, precio, categoría, fecha de expiración, descripción, estado).
- Interfaz amigable con botones de navegación para cambiar entre secciones.
- Validación de datos para los campos de artículos (por ejemplo, el precio debe ser positivo, el estado debe ser 1 o 2).
- Tabla interactiva con desplazamiento para mostrar los registros.

## Requisitos
Para ejecutar esta aplicación, necesitas tener instalado lo siguiente:

- **Python 3.6 o superior**: El lenguaje de programación usado para la aplicación. [Descargar Python](https://www.python.org/downloads/)
- **MySQL Server**: Un servidor MySQL en ejecución para alojar la base de datos. [Descargar MySQL](https://dev.mysql.com/downloads/)
- **Bibliotecas de Python**:
  - `mysql-connector-python`: Para conectar Python con la base de datos MySQL.
  - Tkinter: Incluido en las instalaciones estándar de Python para la interfaz gráfica (no requiere instalación adicional).

## Instalación

1. **Clonar o Descargar el Repositorio**:
   ```bash
   git clone <url-del-repositorio>
   ```
   O descarga los archivos del proyecto manualmente.

2. **Instalar las Dependencias de Python**:
   Instala la biblioteca requerida usando pip:
   ```bash
   pip install mysql-connector-python
   ```

3. **Configurar la Base de Datos MySQL**:
   - Asegúrate de que el servidor MySQL esté en ejecución.
   - Crea la base de datos y las tablas ejecutando el script SQL proporcionado en `Bdd.sql`:
     ```bash
     mysql -u root -p < Bdd.sql
     ```
   - Actualiza las configuraciones de conexión a la base de datos en `clases.py` si es necesario (por ejemplo, cambia `host`, `user`, `passwd` o `database`):
     ```python
     self.cnn = mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="",  # Reemplaza con tu contraseña de MySQL
         database="pharmacydatabase"
     )
     ```

4. **Ejecutar la Aplicación**:
   Navega al directorio del proyecto y ejecuta el script principal:
   ```bash
   python main.py
   ```

## Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación, inicializa la ventana de Tkinter.
- `ventana.py`: Contiene la lógica de la interfaz gráfica, incluyendo formularios, tablas y navegación.
- `clases.py`: Define las clases (`Lab`, `Supp`, `Item`) para las operaciones con la base de datos.
- `Bdd.sql`: Script SQL para crear la base de datos y las tablas.

## Uso
1. Inicia la aplicación ejecutando `python main.py`.
2. Usa los botones de navegación en la parte superior para cambiar entre:
   - **Artículos**: Gestiona los artículos de la farmacia.
   - **Proveedores**: Gestiona los proveedores.
   - **Laboratorios**: Gestiona los laboratorios.
3. En cada sección:
   - Haz clic en **Nuevo** para agregar un nuevo registro.
   - Selecciona un registro y haz clic en **Modificar** para editarlo.
   - Selecciona un registro y haz clic en **Eliminar** para borrarlo.
   - Usa **Guardar** para guardar los cambios o **Cancelar** para descartarlos.
4. La tabla a la derecha muestra todos los registros de la sección seleccionada.

## Requisitos
- **Sistema Operativo**: Windows, macOS o Linux.
- **Versión de Python**: 3.6 o superior.
- **Versión de MySQL**: 5.7 o superior.
- **Bibliotecas de Python**:
  - `mysql-connector-python>=8.0.0`
  - Tkinter (incluido con Python)

## Notas
- Asegúrate de que el servidor MySQL esté en ejecución antes de iniciar la aplicación.
- La aplicación usa una ventana de tamaño fijo (1200x600 píxeles) y no es redimensionable.
- Por seguridad, evita usar el usuario root de MySQL en producción. Crea un usuario dedicado con los permisos adecuados.
- La aplicación utiliza formato de cadenas para las consultas SQL, lo que no es recomendable en producción debido a riesgos de inyección SQL. Considera usar consultas parametrizadas para mayor seguridad.

## Solución de Problemas
- **Error de Conexión a MySQL**: Verifica que el servidor MySQL esté en ejecución y que las configuraciones de conexión (host, usuario, contraseña, base de datos) en `clases.py` sean correctas.
- **Biblioteca Faltante**: Si aparece un error sobre `mysql.connector`, instálalo con `pip install mysql-connector-python`.
- **Tabla Vacía**: Asegúrate de que las tablas de la base de datos se hayan creado ejecutando `Bdd.sql` y de que existan registros en las tablas correspondientes.

## Contribución
¡Siéntete libre de reportar problemas o enviar solicitudes de mejora! Las sugerencias para nuevas funcionalidades o optimizaciones son bienvenidas.

## Licencia
Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).