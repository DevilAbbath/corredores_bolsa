# Plataforma para Corredores de Bolsa

## Descripción
Este proyecto corresponde al examen final de certificacion del bootcamp "DESARROLLO DE APLICACIONES FULL STACK PYTHON TRAINEE V2.0" llamado Corredores de Bolsa donde se evaluaran las habilidades y conocimientos adquiridos durante el Bootcamp.

## Requerimientos

- WSL // Ubuntu
- Django 5.1.3
- Python 3.12+
- PostgreSQL

## Funcionalidad en el Panel de vista web

1. **Iniciar Sesion**: Redirecciona a un form para poder ingresar las credenciales de acceso al sitio.
2. **Cerrar Sesion**: Eliminar del aplicativo la informacion sobre si existe un usuario conectado.
3. **Registrarse**: Usando los forms permitir el ingreso de un nuevo usuario definiendo su funcion y datos adicionales.
4. **Identificacion de Usuario**: En base al tipo de usuario es derivado a su portal 

## Pasos para el montaje

1. **Crear nuestra base de datos**:
    Ingresamos a nuestra shell de psql o bien desde nuestro PGAdmin y creamos nuestra Base de datos con el nombre del proyecto "corredore_bolsa" y creamos nuestro usuario llamado pathuser.

    GUI

    ![Creacion Base de datos](print/instructions/bdcreate.png)

    CLI

   ```bash
   sudo -u postgres psql
   postgres=# CREATE DATABASE corredores_bolsa;
   postgres=# CREATE USER pathuser WITH PASSWORD 'tu_contraseña_segura';
   postgres=# GRANT ALL PRIVILEGES ON DATABASE corredores_bolsa TO pathuser;
   postgres=# \q 


2. **Configuración de la Base de Datos**:

    - Crea la base de datos en PostgreSQL.
    - Configura DATABASES en settings.py.

3. **Migraciones**: 
    Ejecuta las migraciones para crear las tablas en la base de datos:

        ```bash
        python manage.py migrate

4. **Crear un Superusuario**: 
    Para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser

5. **Iniciar el Servidor**: 
    Ejecuta el servidor de desarrollo de Django:

    ```bash
    python manage.py runserver

6. **Acceder al Panel de Admin**: 
    Visita http://127.0.0.1:8000/ para acceder e interectuar con los distintos operadores.


# Resumen del Proyecto de Gestión de Arrendamientos

## 1. **Estructura General y Modelos**
- Se ha creado una aplicación de **gestión de propiedades de arrendamiento** en Django, con funcionalidades para que los **arrendadores** puedan agregar, editar y eliminar inmuebles, mientras que los **arrendatarios** puedan ver propiedades y generar solicitudes de arriendo.
- La base de datos fue configurada correctamente con **PostgreSQL**, con modelos como `Inmueble`, `SolicitudArriendo`, y `UserProfile` que incluyen información sobre propiedades, solicitudes y tipos de usuario.

## 2. **Autenticación y Permisos**
- Se implementó un sistema de **autenticación de usuarios** utilizando Django, permitiendo a los usuarios registrarse, iniciar sesión y cerrar sesión.
- Se usaron permisos personalizados para restringir accesos a vistas y funcionalidades dependiendo del **tipo de usuario** (`arrendador` o `arrendatario`), utilizando decoradores como `@login_required` y `@permission_required`.

## 3. **Interfaz de Usuario**
- Se utilizó **Bootstrap** para mejorar el diseño de las vistas, aplicando clases como `btn`, `table`, `card`, `container`, `w-90` para crear una experiencia más moderna y profesional.
- Se implementaron formularios con el **paquete Crispy Forms**, lo que permitió una visualización de formularios más limpia y profesional con menos código.

## 4. **CRUD de Inmuebles**
- Los **arrendadores** pueden agregar, editar y eliminar inmuebles. Estas acciones están protegidas por permisos, garantizando que solo los arrendadores puedan gestionarlos.
- Se configuraron los botones de eliminación para que usen **modales de confirmación** antes de realizar acciones destructivas, asegurando que los usuarios confirmen sus intenciones antes de eliminar registros importantes.

## 5. **Gestión de Solicitudes de Arriendo**
- Los **arrendatarios** pueden ver un catálogo de inmuebles disponibles y generar **solicitudes de arriendo**. Se ha proporcionado una vista de la solicitud de arriendo con detalles como el nombre, dirección, tipo de inmueble, precio mensual y comuna.
- Las solicitudes de arriendo también tienen un sistema de **gestión de estado**, donde el arrendatario puede ver si su solicitud está pendiente, aceptada o rechazada.
- Los arrendatarios pueden **anular solicitudes** desde la interfaz, con una confirmación de eliminación a través de un modal de Bootstrap.

## 6. **Despliegue y Configuración para Producción**
- **Render** fue elegido como plataforma para el despliegue de tu aplicación. Se preparó tu proyecto para que fuera fácilmente **deployable** con configuraciones de producción:
  - **Archivo `requirements.txt`** para manejar las dependencias del proyecto.
  - **Archivo `Procfile`** para indicarle a Render cómo iniciar la aplicación con `gunicorn`.
  - Configuración para **usar PostgreSQL** como base de datos en producción, utilizando variables de entorno para que la configuración no esté hardcodeada.
  - **Archivos estáticos y de medios** fueron configurados para servir correctamente, y las migraciones de base de datos fueron ejecutadas.

## 7. **Mejoras y Funcionalidades Extras**
- Se mejoró el diseño visual de la página, agregando botones con estilos de Bootstrap y utilizando **modales** para confirmar acciones destructivas.
- Para el manejo de solicitudes, se implementaron botones en el **catálogo de inmuebles** y en las **solicitudes de arriendo** con la funcionalidad de anulación, que ahora también tiene su propia confirmación visual.

## 8. **Plan de Futuro**
- Ahora que el sistema básico está funcional, el siguiente paso sería implementar más características como:
  - **Notificaciones por correo electrónico** para alertar a los arrendadores cuando un arrendatario haga una solicitud.
  - Mejorar la **interacción con los usuarios** con filtros en la vista del catálogo (por precio, tipo de inmueble, etc.).
  - Crear un **panel de administración personalizado** para que los arrendadores gestionen mejor sus propiedades, solicitudes y detalles.

## 9. **Resumen de Tecnologías y Herramientas Usadas**
- **Django** como framework principal para el desarrollo web.
- **PostgreSQL** como base de datos.
- **Bootstrap** para mejorar la apariencia y funcionalidad de la interfaz.
- **Crispy Forms** para un mejor manejo de formularios en la web.
- **Render** para el despliegue de la aplicación en producción.
- **GitHub** para controlar el código y facilitar el despliegue.

Este proyecto ahora está listo para ser probado y lanzado en un entorno de producción con un diseño moderno, funcionalidades clave implementadas, y configurado para escalar en el futuro si es necesario.


---

## **Resultados**
Este proyecto ahora está listo para ser probado y lanzado en un entorno de producción con un diseño moderno, funcionalidades clave implementadas, y configurado para escalar en el futuro si es necesario.



### Print de los resultados

![img1](print/Final/img1.png)

![img2](print/Final/img2.png)

![img3](print/Final/img3.png)

![img4](print/Final/img4.png)

![img4](print/Final/img5.png)

![img4](print/Final/img6.png)

![img4](print/Final/img7.png)

![img4](print/Final/img8.png)

![img4](print/Final/img9.png)

![img4](print/Final/img10.png)

![img4](print/Final/img11.png)


Autor
Nombre: [Erick-Jaime-Jara]
Correo: [alucard.erick.mega@gmail.com]