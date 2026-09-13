**Nombre:** Josue Batallas  
**Materia:** Programación Orientada a Objetos  
**Actividad:** Semana 13

# Restaurante App

La aplicación permite ingresar mediante un usuario y contraseña y, después de iniciar sesión correctamente, acceder a un menú principal donde se pueden consultar los productos y usuarios registrados.

## Objetivo

El objetivo de esta actividad es aplicar los conceptos básicos de las interfaces gráficas de usuario y continuar trabajando con la programación orientada a objetos.

En esta versión se mantiene la organización del proyecto por diferentes partes para que cada archivo tenga una función específica y sea más fácil de entender y modificar.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

## Modelos

En la carpeta `modelos` se encuentran las clases principales del programa.

### Producto

La clase `Producto` representa los productos que se encuentran registrados en el restaurante.

Cada producto tiene:

* Código
* Nombre
* Precio
* Stock

### Usuario

La clase `Usuario` representa a las personas registradas en el sistema.

Cada usuario tiene:

* Identificación
* Nombre
* Contraseña

La contraseña se utiliza para realizar el inicio de sesión de forma simulada dentro de la aplicación.

## Datos

Los datos se guardan en archivos JSON dentro de la carpeta `datos`.

### productos.json

Contiene la información de los productos registrados, como su código, nombre, precio y stock.

### usuarios.json

Contiene la información de los usuarios registrados y sus contraseñas para poder comprobar el acceso a la aplicación.

## Servicios

La carpeta `servicios` contiene las clases encargadas de trabajar con los datos y realizar las operaciones principales.

### ArchivoServicio

Esta clase se encarga de leer los archivos JSON y obtener la información guardada en ellos.

De esta manera, las demás partes del programa no necesitan encargarse directamente de abrir y leer los archivos.

### RestauranteServicio

Esta clase se encarga de cargar los usuarios y productos y convertir los datos obtenidos de los archivos JSON en objetos de las clases `Usuario` y `Producto`.

También permite:

* Validar el usuario y contraseña.
* Obtener la lista de usuarios.
* Obtener la lista de productos.
* Contar los usuarios registrados.
* Contar los productos registrados.

## Interfaz gráfica

Para esta semana se cambió el funcionamiento de la aplicación. Antes se utilizaba un menú en la terminal y ahora se utiliza una interfaz gráfica creada con Tkinter.

### Login

La primera pantalla que aparece es la de inicio de sesión.

Se deben ingresar:

* Usuario
* Contraseña

Si algún campo está vacío, la aplicación muestra un aviso. Si los datos son incorrectos, también muestra un mensaje de error.

Cuando los datos son correctos, se puede ingresar al menú principal.

### Menú principal

Después de iniciar sesión aparece el panel principal de la aplicación.

Desde aquí se pueden utilizar las siguientes opciones:

**Productos:** muestra los productos registrados, incluyendo su código, nombre, precio y stock.

**Usuarios:** muestra los usuarios registrados con su identificación y nombre.

**Ventas:** por el momento esta opción muestra un mensaje indicando que la funcionalidad está pendiente de desarrollo.

**Cerrar sesión:** permite regresar nuevamente a la pantalla de inicio de sesión.

## Organización de la aplicación

Una de las partes importantes de esta actividad fue mantener separadas las diferentes responsabilidades del programa.

Los modelos contienen las clases principales, los servicios se encargan de trabajar con los datos y las vistas se encargan de mostrar la información al usuario.

Las ventanas no leen directamente los archivos JSON, sino que solicitan la información al `RestauranteServicio`.

## Ejecución

Para ejecutar el programa se debe abrir la terminal dentro de la carpeta del proyecto y utilizar:

```text
python main.py
```

Después de ejecutar el programa se abre la ventana de `Restaurante App`.

Para realizar una prueba de acceso se pueden utilizar los datos registrados en `usuarios.json`.

## Estado actual del proyecto

En esta semana se implementó la interfaz gráfica básica utilizando Tkinter y se conectó con los datos que ya tenía el proyecto.

Actualmente se puede:

* Iniciar sesión.
* Mostrar los productos.
* Mostrar los usuarios.
* Consultar la cantidad de productos y usuarios.
* Cerrar sesión.
* Mostrar que la sección de ventas está pendiente.

La funcionalidad de ventas y otras funciones más avanzadas quedan para futuras actividades.

## Conclusión

Con esta actividad pude continuar el proyecto del restaurante y cambiar la forma en que el usuario interactúa con el programa. En lugar de utilizar solamente la terminal, ahora la aplicación cuenta con una ventana gráfica.

También se reforzó la organización del proyecto utilizando modelos, servicios y vistas separadas, lo que permite que el código sea más ordenado y fácil de modificar.
