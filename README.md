# Restaurante App - Semana 11

## Nombre del estudiante

**Josue Batallas**

## Descripción del proyecto

En esta actividad continué trabajando en el proyecto `restaurante_app` que había realizado anteriormente usando Python y programación orientada a objetos.

En esta nueva versión agregué el manejo de ventas, el control de stock y la persistencia de los datos mediante archivos JSON.

El sistema permite registrar usuarios y productos, realizar ventas, consultar las ventas de un usuario y mostrar todas las ventas registradas.

El proyecto está organizado por módulos para mantener cada parte del programa separada y facilitar su mantenimiento.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

## Funcionalidades

El sistema cuenta con las siguientes funciones:

* Registrar usuarios.
* Registrar productos.
* Mostrar usuarios registrados.
* Mostrar productos registrados.
* Realizar ventas.
* Consultar las ventas realizadas por un usuario.
* Mostrar todas las ventas.
* Validar que la cantidad de productos sea mayor que cero.
* Verificar que exista suficiente stock antes de realizar una venta.
* Disminuir el stock cuando la venta se realiza correctamente.
* Guardar la información en archivos JSON.
* Recuperar la información guardada cuando se inicia nuevamente el programa.

## Mejoras realizadas

En esta semana agregué el modelo `Venta`, que permite relacionar un usuario con un producto y registrar la cantidad comprada.

También agregué el archivo `ventas.json`, donde se guardan las ventas realizadas. Además, se mantienen los archivos `productos.json` y `usuarios.json` para guardar los productos y usuarios registrados.

Otra mejora fue implementar el control del stock. Antes de registrar una venta, el programa verifica que el producto y el usuario existan, que la cantidad sea válida y que haya suficiente stock.

Cuando la venta es válida, se registra la venta y se descuenta la cantidad correspondiente del stock del producto.

También agregué una función para consultar las ventas realizadas por un usuario utilizando la colección de objetos `Venta`.

## Uso de programación orientada a objetos

El proyecto utiliza diferentes clases para representar los elementos principales del sistema:

* `Producto`: representa los productos del restaurante y controla su precio y stock.
* `Usuario`: representa a los usuarios registrados.
* `Venta`: relaciona un usuario con un producto y almacena la cantidad vendida.
* `Restaurante`: administra las colecciones de productos, usuarios y ventas.

Las ventas se almacenan como objetos `Venta` dentro de una colección, lo que permite recorrerlas y filtrarlas para consultar las ventas de un usuario específico.

## Persistencia de datos

Para evitar que los datos se pierdan al cerrar el programa, utilicé archivos JSON.

Los archivos utilizados son:

* `productos.json`: almacena los productos y su stock.
* `usuarios.json`: almacena los usuarios registrados.
* `ventas.json`: almacena las ventas realizadas.

Cuando vuelvo a ejecutar el programa, los datos guardados en estos archivos se cargan nuevamente.

## Manejo de errores

El programa cuenta con validaciones para evitar operaciones incorrectas.

Por ejemplo:

* No se permite registrar cantidades menores o iguales a cero.
* No se puede vender una cantidad mayor al stock disponible.
* Se verifica que el usuario exista antes de realizar una venta.
* Se verifica que el producto exista antes de realizar una venta.
* Se controlan errores al leer archivos JSON.
* Se controlan errores de permisos al leer o escribir archivos.

Esto permite que el programa pueda manejar errores previsibles sin cerrarse de manera inesperada.

## Ejecución en Visual Studio Code

Para trabajar con el proyecto utilicé **Visual Studio Code**.

Primero se debe abrir la carpeta `restaurante_app` en Visual Studio Code.

Después se abre la terminal integrada de Visual Studio Code y se ejecuta:

```bash
python main.py
```

Al ejecutar el programa aparece un menú con las diferentes opciones disponibles.

## Pruebas realizadas

Para comprobar el funcionamiento del sistema realicé diferentes pruebas.

### Registro de usuario

Registré un usuario indicando su identificación y nombre. El sistema confirmó que el usuario fue registrado correctamente y la información quedó guardada en `usuarios.json`.

### Registro de producto

Registré un producto indicando su código, nombre, precio y stock. El sistema confirmó el registro y guardó la información en `productos.json`.

### Realización de una venta

Realicé una venta indicando el código del producto, la identificación del usuario y la cantidad.

Cuando los datos fueron correctos y existía suficiente stock, el sistema registró la venta correctamente y disminuyó el stock del producto.

### Validación de stock

También probé realizar una venta con una cantidad mayor al stock disponible.

El sistema rechazó la venta y no realizó ningún descuento en el stock.

### Consulta de ventas

Después de realizar una venta, utilicé la opción de consultar las ventas por usuario.

El sistema recorrió la colección de ventas y mostró las ventas correspondientes al usuario seleccionado.

### Persistencia

Finalmente, cerré el programa y lo ejecuté nuevamente desde Visual Studio Code.

Los usuarios, productos y ventas permanecieron guardados, demostrando que la información se estaba almacenando correctamente en los archivos JSON.

## Conclusión

Con esta actividad pude continuar mejorando el sistema del restaurante y aplicar nuevos conceptos de programación orientada a objetos.

La implementación de la clase `Venta` permitió relacionar usuarios y productos, mientras que el control de stock ayudó a evitar ventas que no se pueden realizar.

También aprendí a utilizar archivos JSON para guardar y recuperar información y a manejar diferentes errores mediante excepciones.
