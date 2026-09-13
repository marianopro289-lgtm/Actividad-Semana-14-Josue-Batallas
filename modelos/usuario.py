class Usuario:
    def __init__(self, identificacion, nombre, contrasena):
        self.identificacion = identificacion
        self.nombre = nombre
        self.contrasena = contrasena

    def __str__(self):
        return f"{self.identificacion} - {self.nombre}"
        