class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if not codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.stock = int(stock)

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente.")

        self.stock -= cantidad

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["precio"],
            datos["stock"]
        )

    def __str__(self) -> str:
        return (
            f"{self.codigo} - {self.nombre} | "
            f"${self.precio:.2f} | Stock: {self.stock}"
        )