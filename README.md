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

La ventana principal tiene diferentes botones

