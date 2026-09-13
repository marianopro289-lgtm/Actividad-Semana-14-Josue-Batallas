import json


class ArchivoServicio:

    def leer_json(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []