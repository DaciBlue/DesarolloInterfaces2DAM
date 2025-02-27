# Instalaciones y Comandos Usados en el Proyecto

Este documento detalla los comandos y librerías utilizadas durante el proyecto, organizados por las clases en las que se emplearon y con notas importantes.

## Clases y Comandos

### Clase 1 y Clase 2

#### Instalación de PySide6
El siguiente comando instala la librería **PySide6**:

```bash
pip install PySide6
```

> [!NOTE]  
> Este comando fue utilizado tanto en la Clase 1 como en la Clase 2.

#### Conversión de un archivo `.ui` a `.py`
El comando a continuación se utilizó en la **Clase 2** para transformar un archivo de interfaz UI a un archivo Python:

```bash
pyside6-uic UI/Clase2InterfazGrupo1.ui -o src/Clase2InterfazGrupo1.py
```

- **Descripción**:
  - `pyside6-uic`: Transforma un archivo `.ui` a un archivo `.py`.
  - `UI/Clase2InterfazGrupo1.ui`: Ruta del archivo `.ui` que queremos convertir.
  - `-o`: Indica el lugar de destino del archivo generado.
  - `src/Clase2InterfazGrupo1.py`: Nueva ruta del archivo convertido con extensión `.py`.

---

### Clase 7

#### Instalación de `datapane` y Dependencias
Para instalar la librería **datapane** se siguieron estos pasos:

```bash
pip install datapane
```

> [!NOTE]  
> Antes de realizar esta instalación, fue necesario aplicar los siguientes pasos:  
> 1. Borrar la carpeta `.venv`.  
> 2. Instalar Python 3.9 en el entorno virtual.  
> 3. Actualizar `pip`:  
>    ```bash
>    python.exe -m pip install --upgrade pip
>    ```
> 4. Instalar versiones específicas de las librerías siguientes:
>    ```bash
>    pip install numpy==1.23.5 pandas==1.5.3
>    pip install PySide6
>    pip install PyInstaller
>    ```

> [!TIP]  
> Esto fue realizado correctamente gracias a la sugerencia de **Juanma**.

---

### Clase 8

#### Instalación de Pytest para Tests Automáticos
El paquete **pytest** se utilizó para realizar pruebas automáticas:

```bash
pip install pytest
```

##### Ejecución de Tests
Para ejecutar pruebas usando un ejemplo en la carpeta `test`:

```bash
pytest test/test_task_managerClase8.py
```

> [!NOTE]  
> Si el proyecto está en `src` y los tests en la carpeta `test`, es necesario configurar el acceso de `pytest` al directorio del proyecto agregando este comando en el script de test:
> 
> ```python
> sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
> ```

> [!TIP]  
> En caso de que el proyecto y los tests estén en la misma carpeta (por ejemplo, todo en `src`), no es necesario usar esta configuración adicional. El siguiente comando sería suficiente:
>
> ```bash
> pytest src/test_task_managerClas8.py
> ```

---

### Generación de un Archivo Ejecutable (.EXE)

Para crear un archivo ejecutable a partir de un script en Python, sigue estos pasos:

1. **Instalar la librería `pyinstaller`:**

   ```bash
   pip install pyinstaller
   ```

2. **Generar el ejecutable:**

   ```bash
   pyinstaller --onefile --windowed InterfazPrueba.py
   ```

> [!NOTE]  
> - `--onefile`: Genera un solo archivo ejecutable.  
> - `--windowed`: Elimina la consola al ejecutar el archivo `.exe` generado.

---

## Conclusión
Este documento reúne los comandos y prácticas utilizadas en el proyecto, organizadas por clase, y complementadas con notas y tips para aclaraciones y buen uso futuro.