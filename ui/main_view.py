import tkinter as tk
from tkinter import ttk, messagebox


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
        titulo.pack(pady=15)

        subtitulo = tk.Label(
            self.frame,
            text="Panel principal"
        )
        subtitulo.pack()

        navegacion = tk.Frame(self.frame)
        navegacion.pack(pady=15)

        tk.Button(
            navegacion,
            text="Productos",
            width=18,
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            navegacion,
            text="Usuarios",
            width=18,
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            navegacion,
            text="Ventas",
            width=18,
            command=self.ventas_pendientes
        ).grid(row=0, column=2, padx=5)

        self.info_label = tk.Label(
            self.frame,
            text=""
        )
        self.info_label.pack(pady=10)

        tk.Button(
            self.frame,
            text="Cerrar sesión",
            width=20,
            command=self.cerrar_sesion
        ).pack(pady=10)

        self.actualizar_informacion()

    def actualizar_informacion(self):
        self.info_label.config(
            text=(
                f"Usuarios registrados: "
                f"{self.servicio.cantidad_usuarios()}    |    "
                f"Productos registrados: "
                f"{self.servicio.cantidad_productos()}"
            )
        )

    def mostrar_productos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de productos")
        ventana.geometry("750x600")

        titulo = tk.Label(
            ventana,
            text="Gestión de productos",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=10)

        formulario = tk.LabelFrame(
            ventana,
            text="Datos del producto",
            padx=10,
            pady=10
        )
        formulario.pack(fill="x", padx=20, pady=10)

        tk.Label(formulario, text="Código:").grid(
            row=0, column=0, padx=5, pady=5
        )

        codigo_entry = tk.Entry(formulario, width=25)
        codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario, text="Nombre:").grid(
            row=1, column=0, padx=5, pady=5
        )

        nombre_entry = tk.Entry(formulario, width=25)
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario, text="Precio:").grid(
            row=2, column=0, padx=5, pady=5
        )

        precio_entry = tk.Entry(formulario, width=25)
        precio_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario, text="Stock:").grid(
            row=3, column=0, padx=5, pady=5
        )

        stock_entry = tk.Entry(formulario, width=25)
        stock_entry.grid(row=3, column=1, padx=5, pady=5)

        botones = tk.Frame(ventana)
        botones.pack(pady=10)

        tabla_frame = tk.Frame(ventana)
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columnas = ("codigo", "nombre", "precio", "stock")

        tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")
        tabla.heading("stock", text="Stock")

        tabla.column("codigo", width=100)
        tabla.column("nombre", width=220)
        tabla.column("precio", width=100)
        tabla.column("stock", width=100)

        tabla.pack(fill="both", expand=True)

        def limpiar_campos():
            codigo_entry.delete(0, tk.END)
            nombre_entry.delete(0, tk.END)
            precio_entry.delete(0, tk.END)
            stock_entry.delete(0, tk.END)

        def cargar_tabla():
            for item in tabla.get_children():
                tabla.delete(item)

            productos = self.servicio.listar_productos()

            for producto in productos:
                tabla.insert(
                    "",
                    tk.END,
                    values=(
                        producto.codigo,
                        producto.nombre,
                        f"{producto.precio:.2f}",
                        producto.stock
                    )
                )

            self.actualizar_informacion()

        def registrar():
            codigo = codigo_entry.get().strip()
            nombre = nombre_entry.get().strip()
            precio = precio_entry.get().strip()
            stock = stock_entry.get().strip()

            if not codigo or not nombre or not precio or not stock:
                messagebox.showwarning(
                    "Datos incompletos",
                    "Complete todos los campos."
                )
                return

            try:
                precio = float(precio)
                stock = int(stock)
            except ValueError:
                messagebox.showerror(
                    "Datos incorrectos",
                    "El precio debe ser numérico y el stock debe ser entero."
                )
                return

            self.servicio.registrar_producto(
                codigo,
                nombre,
                precio,
                stock
            )

            cargar_tabla()
            limpiar_campos()

            messagebox.showinfo(
                "Producto registrado",
                "El producto se registró correctamente."
            )

        def consultar():
            codigo = codigo_entry.get().strip()

            if not codigo:
                messagebox.showwarning(
                    "Código",
                    "Ingrese el código del producto."
                )
                return

            for producto in self.servicio.listar_productos():
                if producto.codigo == codigo:
                    nombre_entry.delete(0, tk.END)
                    nombre_entry.insert(0, producto.nombre)

                    precio_entry.delete(0, tk.END)
                    precio_entry.insert(0, producto.precio)

                    stock_entry.delete(0, tk.END)
                    stock_entry.insert(0, producto.stock)

                    return

            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese código."
            )

        def actualizar():
            codigo = codigo_entry.get().strip()
            nombre = nombre_entry.get().strip()
            precio = precio_entry.get().strip()
            stock = stock_entry.get().strip()

            if not codigo or not nombre or not precio or not stock:
                messagebox.showwarning(
                    "Datos incompletos",
                    "Complete todos los campos."
                )
                return

            try:
                precio = float(precio)
                stock = int(stock)
            except ValueError:
                messagebox.showerror(
                    "Datos incorrectos",
                    "El precio debe ser numérico y el stock debe ser entero."
                )
                return

            actualizado = self.servicio.actualizar_producto(
                codigo,
                nombre,
                precio,
                stock
            )

            if actualizado:
                cargar_tabla()
                limpiar_campos()

                messagebox.showinfo(
                    "Producto actualizado",
                    "El producto se actualizó correctamente."
                )
            else:
                messagebox.showerror(
                    "Producto no encontrado",
                    "No existe un producto con ese código."
                )

        def eliminar():
            codigo = codigo_entry.get().strip()

            if not codigo:
                messagebox.showwarning(
                    "Código",
                    "Ingrese el código del producto."
                )
                return

            eliminado = self.servicio.eliminar_producto(codigo)

            if eliminado:
                cargar_tabla()
                limpiar_campos()

                messagebox.showinfo(
                    "Producto eliminado",
                    "El producto se eliminó correctamente."
                )
            else:
                messagebox.showerror(
                    "Producto no encontrado",
                    "No existe un producto con ese código."
                )

        tk.Button(
            botones,
            text="Registrar",
            width=14,
            command=registrar
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botones,
            text="Consultar",
            width=14,
            command=consultar
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botones,
            text="Actualizar",
            width=14,
            command=actualizar
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botones,
            text="Eliminar",
            width=14,
            command=eliminar
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            botones,
            text="Limpiar",
            width=14,
            command=limpiar_campos
        ).grid(row=0, column=4, padx=5)

        cargar_tabla()

    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()

        ventana = tk.Toplevel(self.root)
        ventana.title("Usuarios")
        ventana.geometry("500x350")

        tk.Label(
            ventana,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tabla = ttk.Treeview(
            ventana,
            columns=("identificacion", "nombre"),
            show="headings"
        )

        tabla.heading("identificacion", text="Identificación")
        tabla.heading("nombre", text="Nombre")

        tabla.column("identificacion", width=150)
        tabla.column("nombre", width=250)

        tabla.pack(fill="both", expand=True, padx=20, pady=10)

        for usuario in usuarios:
            tabla.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre
                )
            )

    def ventas_pendientes(self):
        messagebox.showinfo(
            "Ventas",
            "La funcionalidad de ventas está pendiente de desarrollo."
        )
        