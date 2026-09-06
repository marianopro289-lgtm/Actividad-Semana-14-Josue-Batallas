from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n===== RESTAURANTE APP - SEMANA 12 =====")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Mostrar usuarios")
    print("4. Mostrar productos")
    print("5. Realizar venta")
    print("6. Consultar ventas por usuario")
    print("7. Mostrar todas las ventas")
    print("0. Salir")


def registrar_usuario(restaurante: Restaurante) -> None:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()

    try:
        if restaurante.registrar_usuario(
            identificacion,
            nombre
        ):
            print("Usuario registrado correctamente.")
        else:
            print("Ya existe un usuario con esa identificación.")

    except ValueError as error:
        print(f"Error: {error}")


def registrar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre del producto: ").strip()

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        if restaurante.registrar_producto(
            codigo,
            nombre,
            precio,
            stock
        ):
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"Error: {error}")


def mostrar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n--- USUARIOS ---")

    for usuario in usuarios:
        print(usuario)


def mostrar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- PRODUCTOS ---")

    for producto in productos:
        print(producto)


def realizar_venta(restaurante: Restaurante) -> None:
    codigo_producto = input(
        "Código del producto: "
    ).strip()

    identificacion_usuario = input(
        "Identificación del usuario: "
    ).strip()

    try:
        cantidad = int(
            input("Cantidad: ")
        )

        if restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        ):
            print("Venta registrada correctamente.")
        else:
            print(
                "No se pudo realizar la venta. "
                "Verifique usuario, producto, "
                "cantidad y stock."
            )

    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:

    identificacion = input(
        "Identificación del usuario: "
    ).strip()

    if restaurante.buscar_usuario(
        identificacion
    ) is None:

        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    if not ventas:
        print(
            "El usuario no tiene ventas registradas."
        )
        return

    print("\n--- VENTAS DEL USUARIO ---")

    for venta in ventas:

        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            nombre_producto = producto.nombre
        else:
            nombre_producto = "Producto no encontrado"

        print(
            f"Producto: {nombre_producto} | "
            f"Código: {venta.producto_codigo} | "
            f"Cantidad: {venta.cantidad}"
        )


def mostrar_ventas(restaurante: Restaurante) -> None:
    ventas = restaurante.listar_ventas()

    if not ventas:
        print("No hay ventas registradas.")
        return

    print("\n--- TODAS LAS VENTAS ---")

    for venta in ventas:
        print(venta)


def main() -> None:
    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        try:

            if opcion == "1":
                registrar_usuario(restaurante)

            elif opcion == "2":
                registrar_producto(restaurante)

            elif opcion == "3":
                mostrar_usuarios(restaurante)

            elif opcion == "4":
                mostrar_productos(restaurante)

            elif opcion == "5":
                realizar_venta(restaurante)

            elif opcion == "6":
                consultar_ventas_usuario(restaurante)

            elif opcion == "7":
                mostrar_ventas(restaurante)

            elif opcion == "0":
                print("Programa finalizado.")
                break

            else:
                print("Opción no válida.")

        except (PermissionError, OSError) as error:
            print(f"Error de archivo: {error}")


if __name__ == "__main__":
    main()