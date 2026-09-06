# Restaurante App - Semana 12

**Nombre:** Josue Batallas  
**Materia:** Programación Orientada a Objetos  
**Actividad:** Semana 12

## Descripción del proyecto

Este proyecto es una continuación del sistema `restaurante_app` que realicé en la Semana 11.

El sistema permite registrar usuarios, registrar productos, realizar ventas, consultar las ventas de un usuario y controlar el stock de los productos.

En esta semana mantuve la estructura que ya tenía y realicé mejoras en la forma en que el programa busca y consulta la información. La idea principal fue evitar recorrer las listas completas cuando ya se conoce un código o una identificación.

## Mejoras realizadas

La principal mejora fue agregar diccionarios como índices en memoria para hacer más rápidas algunas búsquedas.

Se mantienen las listas de productos, usuarios y ventas porque siguen siendo necesarias para almacenar los objetos, mostrarlos y guardar la información en los archivos JSON.

### Búsqueda de productos

Antes, para buscar un producto por su código se recorría toda la lista de productos.

Ahora se utiliza un diccionario llamado:

`_productos_por_codigo`

El código del producto funciona como clave y el objeto `Producto` queda como valor. De esta manera, cuando necesito buscar un producto, puedo obtenerlo directamente usando su código.

### Búsqueda de usuarios

También se mejoró la búsqueda de usuarios mediante el diccionario:

`_usuarios_por_identificacion`

La identificación del usuario se utiliza como clave. Esto permite encontrar un usuario sin tener que recorrer todos los usuarios registrados.

### Consulta de ventas por usuario

También mejoré la consulta de ventas. Para esto utilicé el diccionario:

`_ventas_por_usuario`

En este diccionario cada usuario tiene asociada una lista con sus ventas.

Así, cuando se quieren consultar las ventas de un usuario, no es necesario revisar todas las ventas registradas. Se puede acceder directamente a las ventas relacionadas con esa identificación.

## Colecciones utilizadas

En el proyecto se utilizan principalmente:

- **Listas:** se mantienen para almacenar productos, usuarios y ventas, además de permitir recorrerlos, listarlos y guardarlos en JSON.
- **Diccionarios:** se utilizan como índices para mejorar las búsquedas y consultas frecuentes.
- **Set:** no fue necesario utilizarlo porque en este proyecto no encontré una validación donde aportara una mejora real.

Los diccionarios utilizados son:

- `_productos_por_codigo`
- `_usuarios_por_identificacion`
- `_ventas_por_usuario`

## Sincronización de los índices

Los índices se actualizan cuando se agregan nuevos usuarios o productos.

También se actualiza el índice de ventas cuando se realiza una nueva venta.

Además, al iniciar el programa se cargan los datos guardados en los archivos JSON y después se reconstruyen nuevamente los índices. Esto permite que los diccionarios tengan la información actual aunque el programa se haya cerrado anteriormente.

## Persistencia de datos

El proyecto mantiene la persistencia mediante archivos JSON:

- `productos.json`
- `usuarios.json`
- `ventas.json`

Los datos se guardan cuando se registran productos, usuarios o ventas, y pueden recuperarse nuevamente al ejecutar el programa.

## Control de stock

El control de stock se mantiene igual que en la versión anterior.

Cuando se realiza una venta, primero se verifica que el usuario y el producto existan y que haya suficiente stock. Después se registra la venta y se descuenta la cantidad vendida del stock del producto.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
