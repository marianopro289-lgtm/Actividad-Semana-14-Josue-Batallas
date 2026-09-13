import tkinter as tk
from tkinter import messagebox


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.crear_interfaz()

    def crear_interfaz(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        titulo = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=20)

        bienvenida = tk.Label(
            self.frame,
            text="Panel principal"
        )
        bienvenida.pack(pady=5)

        botones_frame = tk.Frame(self.frame)
        botones_frame.pack(pady=20)

        tk.Button(
            botones_frame,
            text="Productos",
            width=20,
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones_frame,
            text="Usuarios",
            width=20,
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            botones_frame,
            text="Ventas",
            width=20,
            command=self.ventas_pendientes
        ).grid(row=0, column=2, padx=10)

        tk.Button(
            self.frame,
            text="Cerrar sesión",
            width=20,
            command=self.cerrar_sesion
        ).pack(pady=30)

        self.info_label = tk.Label(
            self.frame,
            text=(
                f"Usuarios registrados: "
                f"{self.servicio.cantidad_usuarios()}    |    "
                f"Productos registrados: "
                f"{self.servicio.cantidad_productos()}"
            )
        )
        self.info_label.pack(pady=10)

    def mostrar_productos(self):
        productos = self.servicio.listar_productos()

        ventana = tk.Toplevel(self.root)
        ventana.title("Productos")
        ventana.geometry("550x400")

        tk.Label(
            ventana,
            text="Productos registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        if not productos:
            tk.Label(
                ventana,
                text="No hay productos registrados."
            ).pack()
            return

        for producto in productos:
            texto = (
                f"Código: {producto.codigo} | "
                f"{producto.nombre} | "
                f"${producto.precio:.2f} | "
                f"Stock: {producto.stock}"
            )

            tk.Label(
                ventana,
                text=texto,
                anchor="w"
            ).pack(fill="x", padx=20, pady=3)

    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()

        ventana = tk.Toplevel(self.root)
        ventana.title("Usuarios")
        ventana.geometry("450x350")

        tk.Label(
            ventana,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        if not usuarios:
            tk.Label(
                ventana,
                text="No hay usuarios registrados."
            ).pack()
            return

        for usuario in usuarios:
            texto = (
                f"Identificación: {usuario.identificacion} | "
                f"Nombre: {usuario.nombre}"
            )

            tk.Label(
                ventana,
                text=texto,
                anchor="w"
            ).pack(fill="x", padx=20, pady=5)

    def ventas_pendientes(self):
        messagebox.showinfo(
            "Ventas",
            "La funcionalidad de ventas está pendiente de desarrollo."
        )
        