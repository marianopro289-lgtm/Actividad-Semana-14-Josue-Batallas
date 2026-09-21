# Restaurante App

**Nombre:** Josue Batallas
**Materia:** Programación Orientada a Objetos
**Semana:** 14

## Inicio de sesión

En esta semana también se corrigió el problema que se había presentado anteriormente con el inicio de sesión.

Ahora el programa permite ingresar correctamente utilizando un usuario y una contraseña que estén registrados en el archivo `usuarios.json`.

Para realizar una prueba de ingreso se puede utilizar:

* **Usuario:** `Josue`
* **Contraseña:** `1234`

Después de ingresar correctamente, se muestra el panel principal de la aplicación.

## Sobre el proyecto

Este proyecto es la continuación de la aplicación de restaurante que se ha ido realizando durante las semanas anteriores.

En esta semana continué trabajando con la interfaz gráfica utilizando Tkinter. También agregué nuevas funciones para poder administrar los productos desde la misma aplicación.

La idea fue mantener la estructura que ya tenía el proyecto y agregar las nuevas funciones sin tener que hacerlo nuevamente desde cero.

## Estructura del proyecto

```text
restaurante_app/
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

## Interfaz gráfica

Para esta actividad seguí utilizando Tkinter para la parte visual del programa.

La ventana principal tiene diferentes botones para acceder a las funciones de la aplicación. También se organizaron mejor los elementos utilizando marcos y diferentes componentes de Tkinter.

En la sección de productos se agregó un formulario donde se pueden ingresar los datos de cada producto.

También se utiliza una tabla para poder visualizar los productos registrados de una manera más ordenada.

## Administración de productos

Una de las partes principales de esta semana fue agregar las operaciones básicas para administrar los productos.

Ahora se puede:

* Registrar un producto.
* Consultar un producto por su código.
* Actualizar los datos de un producto.
* Eliminar un producto.
* Ver los productos registrados en una tabla.
* Limpiar los campos del formulario.

Después de realizar una operación, la tabla se actualiza para mostrar la información actualizada.

## Guardado de los productos

Los productos se guardan en:

```text
datos/productos.json
```

Anteriormente el programa podía leer la información del archivo, pero para esta actividad también agregué la opción de guardar los cambios.

De esta manera, cuando registro, actualizo o elimino un producto, los cambios se guardan en el archivo JSON.

También comprobé que al cerrar el programa y volverlo a abrir, los cambios realizados permanecen guardados.

## Usuarios

Los usuarios se encuentran registrados en:

```text
datos/usuarios.json
```

La aplicación utiliza estos datos para comprobar el usuario y la contraseña durante el inicio de sesión.

También se mantiene la opción de consultar los usuarios desde el panel principal.

## Servicios

Las operaciones de los productos se realizan desde `RestauranteServicio`.

Esto permite que la interfaz se encargue principalmente de mostrar los datos y recibir la información del usuario, mientras que el servicio se encarga d

