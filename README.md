# Prueba Técnica QA Automation - Redarbor con Selenium y Python. Realizada en Page Object Model(POM)

## Descarga e Instalación:
### Para clonar el repositorio se deberán de realizar los siguientes pasos: 
* Como requisito previo, se debe de tener instalado y actualizado Python, en mi caso, la version 3.12.0, así como pip a la versión 23.2.1
* Escribir en la terminal: `git clone https://github.com/Frederic2047/redarbor.git`.  
* Una vez clonado el repositorio, lo abrimos a través del IDE correspondiente (Visual Studio Code, Pycharm...).
* Dentro del IDE, abrimos una terminal nueva e instalamos Selenium: `pip install selenium`
* Instalamos pytest: `pip install -U pytest`
* Instalamos la extensión --html para los reportes: `pip install pytest-html`
## Estructura del Proyecto:
* `.idea/` Contiene configuraciones internas del editor.
* `pytests_cache/` Contiene archivos con logs "en caché" de pruebas fallidas. Se crean varias carpetas como esta en varios puntos del proyecto. Aparecerá tras ejecutar la primera vez la prueba.
* `reports/` Contiene las capturas de pantalla que se generan en caso de que los assertions fallen. También contiene el report.html que es un informe detallado al ejecutarse el test al completo, el cual nos muestra si ha sido "Pass" o "Fail" y porqué. 
* `src/` 
    * `PageObject/` Contiene archivos de prueba. 
        * `Pages/` Contiene archivos de prueba.
            * `credentials.json/` Contiene los datos sensibles en un archivo .json.
            * `HomePage.py/` Contiene todas las variables encapsuladas, getters y acciones del proyecto.
    * `TestBase/`
        * `WebDriverSetup.py` Contiene el código mediante el cual creamos una instancia de nuestro navegador en la clase principal.
* `tests/` Contiene las pruebas del proyecto. 
    * `__init__.py` Archivo .py vacío, necesario para lanzar los tests.
    * `test_search_job_offer.py` Contiene todas las pruebas del proyecto.
* `venv` Contiene archivos del entorno virtual.
* `pytest.ini` Archivo desde el cual se configura qué clases, funciones y archivos se ejecutan al lanzar la prueba. Pytest vendrá aqui a buscar la configuración y los markers (en caso de haberlos).
* `README.md` Información acerca de la descarga y puesta en marcha del proyecto.


## Ejecución de Pruebas: 
### Mediante el archivo pytest.ini, se ha configurado que se lanzen automáticamente todos los archivos cuyo nombre comience por: "test_*", todas las clases cuyo nombre "Test*" y todas las funciones cuyo nombre comience por "test_*". Dicho esto:

### Opción 1: Pytest:
* Para ejecutar las pruebas sin impresiones de consola y sin generación del archivo informe, escribir en la terminal : `pytest`
* Automáticamente comenzará a realizar la prueba.
* Al finalizar, nos lanzará en la terminal un log conforme la prueba ha pasado y el tiempo de ejecución.

### Opción 2: Pytest con información adicional:
* Para que pytest nos emita información adicional, de la prueba, deberemos escribir los siguientes parametros:
    * `pytest -v -s`
* El resultado de la prueba nos aparecerá en la propia terminal con -v "verbose", de forma un poco más detallada 
* El parámetro -s nos realizará los print internos de la aplicación, mostrándolos en consola, para tener incluso más información de la prueba.  

### Opción 3: Pytest con información adicional y generación de archivo reporte:
* Esta opción es la más completa, pytest nos emitirá además de la información adicional "opción 2", un informe llamado report.html guardado en la carpeta reports/:
    * `pytest -s -v --html=reports/report.html`
* Este informe se puede arrastrar a una pestaña de un navegador y nos mostrará una estructura html básica detallando el entorno y diferentes parámetros de la prueba.

## Errores: 
* En caso de suceder un error en las assertions, se generará automáticamente una captura de pantalla, que facilita posteriormente ver el lugar en el cual ha ocurrido el error.
* Esta captura se aloja en la carpeta `reports/`.
* Tanto los reportes como las Screenshots, se sobrescriben cada vez que lanzemos la prueba. 
* Para forzar una screenshot por ejemplo, se puede acudir al archivo HomePage.py, y en la línea 156 cambiamos el siguiente texto: '{self.city}' por 'hola' por ejemplo, esto nos dará un "NoSuchElementException" y nos entrará en el except, generándonos un screenshot. 
