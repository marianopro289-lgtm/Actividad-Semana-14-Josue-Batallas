import json
from pathlib import Path
from typing import Any


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos"):
        self.carpeta_datos = Path(carpeta_datos)
        self.carpeta_datos.mkdir(parents=True, exist_ok=True)

    def guardar(self, nombre_archivo: str, datos: list[dict[str, Any]]) -> None:
        ruta = self.carpeta_datos / nombre_archivo

        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )
        except PermissionError as error:
            raise PermissionError(
                f"No hay permisos para escribir en {ruta}."
            ) from error

    def cargar(self, nombre_archivo: str) -> list[dict[str, Any]]:
        ruta = self.carpeta_datos / nombre_archivo

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                raise ValueError(
                    f"El archivo {nombre_archivo} debe contener una lista JSON."
                )

            return datos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            raise ValueError(
                f"El archivo {nombre_archivo} contiene JSON inválido."
            ) from error

        except PermissionError as error:
            raise PermissionError(
                f"No hay permisos para leer {ruta}."
            ) from error
            