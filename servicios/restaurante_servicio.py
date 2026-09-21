from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        self.archivo_servicio = ArchivoServicio()

        self.usuarios = []
        self.productos = []

        self.cargar_usuarios()
        self.cargar_productos()

    def cargar_usuarios(self):
        datos = self.archivo_servicio.leer_json("datos/usuarios.json")

        self.usuarios = [
            Usuario(
                usuario["identificacion"],
                usuario["nombre"],
                usuario["contrasena"]
            )
            for usuario in datos
        ]

    def cargar_productos(self):
        datos = self.archivo_servicio.leer_json("datos/productos.json")

        self.productos = [
            Producto(
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            )
            for producto in datos
        ]

    def validar_acceso(self, identificacion, contrasena):
        for usuario in self.usuarios:
            if (
                usuario.identificacion == identificacion
                and usuario.contrasena == contrasena
            ):
                return True

        return False

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def registrar_producto(self, codigo, nombre, precio, stock):
        nuevo_producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self.productos.append(nuevo_producto)
        self.guardar_productos()

    def actualizar_producto(self, codigo, nombre, precio, stock):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.nombre = nombre
                producto.precio = precio
                producto.stock = stock

                self.guardar_productos()
                return True

        return False

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                self.guardar_productos()
                return True

        return False

    def guardar_productos(self):
        datos = []

        for producto in self.productos:
            datos.append({
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            })

        self.archivo_servicio.guardar_json(
            "datos/productos.json",
            datos
        )