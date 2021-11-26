.. DjangoProject documentation master file, created by
   sphinx-quickstart on Fri Nov 26 16:36:42 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DjangoProject - Practicas AIATIC 2021-2
=======================================

Introducción
************

En la presente documentación encontrará toda la información relacionada con el proyecto
**DjangoProject**, aplicativo desarrollado en el trascurso del último mes de la práctica profesional en Ingenería de Sitemas en la empresa **A&A SOLUCIONES TIC**.

Carácteristicas
***************

* Sitio Web
* Registro local y Autenticación con Facebook, Google y Github
* CRUD para tableros de dos tipos: 'público' o 'privado
* CRUD para ideas en tablero correspondiente
* Restriccion de propiedad de tableros o ideas
* Interfaz intuitiva
* Diseño Responsivo

Tecnologias implementadas
*************************
A continuación se listarán las tecnologias y librerias implementadas para el desarrollo del presente proyecto:

* **Front-end**
    * Bootstrap v5.1.3
    * JavaScript
    * JQuery v3.3.1

* **Back-end**
    * Django v3.2.9

* **Control de versiones**
    * Git

* **Documentación**
    * Sphinx

* **Librerias implementadas**
    * django-allauth v0.46.0
    * djangorestframework 3.12.4
    * django-bootstrap-modal-forms v2.2.0
    * django-crispy-forms v1.13.0
    * django-active-link v0.1.8

* **Bases de datos**
    * PostgreSQL
    * psycopg2 v2.9.2

Configuración Inicial
*********************

Para ejecutar el proyecto se sugiere seguir los siguientes pasos:


   1. Crear un entorno virtual

   2. Clonar el proyecto desde el repositorio alojado en Github:
      git clone  https://github.com/dev20-aiatic/djangoproject

   3. Instalar  lista de dependencias ``pip install -r requirements.txt``

   4. Dirigirse a la configuración del proyecto en ``djangoProject/settings.py``
      modificar atributos ``SECRET_KEY`` y ``DATABASE``.

   5. Efectuar la creación de tablas de la base datos ``manage.py migrate``

   6. Una vez se completen los anteriores pasos, puede ejecutar el servidor local
      de Django ``manage.py runserver``

   7. Abrir su navegador y dirigirse a http://127.0.0.1:8000 para empezar a hacer uso del
      aplicativo.

.. toctree::
   :maxdepth: 2
   :caption: Contenido:

   ejercicio1/index
   ejercicio2/index
   ejercicio3/index
