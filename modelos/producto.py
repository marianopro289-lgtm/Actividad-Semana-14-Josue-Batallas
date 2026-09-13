class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (
            f"{self.codigo} - {self.nombre} - "
            f"${self.precio:.2f} - Stock: {self.stock}"
        )