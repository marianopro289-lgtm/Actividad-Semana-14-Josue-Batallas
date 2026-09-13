import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.crear_interfaz()

    def crear_interfaz(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        titulo = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            self.frame,
            text="Inicio de sesión"
        )
        subtitulo.pack(pady=5)

        tk.Label(
            self.frame,
            text="Usuario:"
        ).pack()

        self.usuario_entry = tk.Entry(
            self.frame,
            width=30
        )
        self.usuario_entry.pack(pady=5)

        tk.Label(
            self.frame,
            text="Contraseña:"
        ).pack()

        self.contrasena_entry = tk.Entry(
            self.frame,
            width=30,
            show="*"
        )
        self.contrasena_entry.pack(pady=5)

        boton = tk.Button(
            self.frame,
            text="Ingresar",
            width=20,
            command=self.iniciar_sesion
        )
        boton.pack(pady=20)

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )
            return

        if self.servicio.validar_acceso(usuario, contrasena):
            self.frame.destroy()
            self.mostrar_principal()
        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )