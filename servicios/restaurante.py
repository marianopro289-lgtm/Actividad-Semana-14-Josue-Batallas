from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        # Índices auxiliares para mejorar el rendimiento
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

        self._archivo_servicio = ArchivoServicio()

        self.cargar_datos()

        # Reconstruir los índices después de cargar los datos
        self.reconstruir_indices()

    # ==============================
    # ÍNDICES AUXILIARES
    # ==============================

    def reconstruir_indices(self) -> None:
        self._productos_por_codigo = {
            producto.codigo: producto
            for producto in self._productos
        }

        self._usuarios_por_identificacion = {
            usuario.identificacion: usuario
            for usuario in self._usuarios
        }

        self._ventas_por_usuario = {}

        for venta in self._ventas:
            if venta.usuario_id not in self._ventas_por_usuario:
                self._ventas_por_usuario[venta.usuario_id] = []

            self._ventas_por_usuario[venta.usuario_id].append(venta)

    # ==============================
    # PRODUCTOS
    # ==============================

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ) -> bool:

        if self.buscar_producto(codigo) is not None:
            return False

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self._productos.append(producto)

        # Actualizar índice de productos
        self._productos_por_codigo[producto.codigo] = producto

        self.guardar_productos()

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:

        # Búsqueda rápida mediante diccionario
        return self._productos_por_codigo.get(
            codigo.strip()
        )

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    # ==============================
    # USUARIOS
    # ==============================

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str
    ) -> bool:

        if self.buscar_usuario(identificacion) is not None:
            return False

        usuario = Usuario(
            identificacion,
            nombre
        )

        self._usuarios.append(usuario)

        # Actualizar índice de usuarios
        self._usuarios_por_identificacion[
            usuario.identificacion
        ] = usuario

        self.guardar_usuarios()

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        # Búsqueda rápida mediante diccionario
        return self._usuarios_por_identificacion.get(
            identificacion.strip()
        )

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    # ==============================
    # VENTAS
    # ==============================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        # Las búsquedas utilizan los índices auxiliares
        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None or producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        # Actualizar índice de ventas por usuario
        if usuario.identificacion not in self._ventas_por_usuario:
            self._ventas_por_usuario[
                usuario.identificacion
            ] = []

        self._ventas_por_usuario[
            usuario.identificacion
        ].append(venta)

        # Actualizar stock
        producto.vender(cantidad)

        self.guardar_ventas()
        self.guardar_productos()

        return True

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        # Consulta rápida mediante índice
        return self._ventas_por_usuario.get(
            identificacion_usuario.strip(),
            []
        ).copy()

    def listar_ventas(self) -> list[Venta]:
        return self._ventas.copy()

    # ==============================
    # GUARDAR DATOS
    # ==============================

    def guardar_productos(self) -> None:

        datos = [
            producto.convertir_a_diccionario()
            for producto in self._productos
        ]

        self._archivo_servicio.guardar(
            "productos.json",
            datos
        )

    def guardar_usuarios(self) -> None:

        datos = [
            usuario.convertir_a_diccionario()
            for usuario in self._usuarios
        ]

        self._archivo_servicio.guardar(
            "usuarios.json",
            datos
        )

    def guardar_ventas(self) -> None:

        datos = [
            venta.convertir_a_diccionario()
            for venta in self._ventas
        ]

        self._archivo_servicio.guardar(
            "ventas.json",
            datos
        )

    # ==============================
    # CARGAR DATOS
    # ==============================

    def cargar_datos(self) -> None:

        try:

            datos_productos = self._archivo_servicio.cargar(
                "productos.json"
            )

            datos_usuarios = self._archivo_servicio.cargar(
                "usuarios.json"
            )

            datos_ventas = self._archivo_servicio.cargar(
                "ventas.json"
            )

            self._productos = [
                Producto.desde_diccionario(datos)
                for datos in datos_productos
            ]

            self._usuarios = [
                Usuario.desde_diccionario(datos)
                for datos in datos_usuarios
            ]

            self._ventas = [
                Venta.desde_diccionario(datos)
                for datos in datos_ventas
            ]

        except (KeyError, ValueError, PermissionError) as error:

            print(f"Error al cargar los datos: {error}")

            self._productos = []
            self._usuarios = []
            self._ventas = []