class Proyecto:
    def __init__(self, id_proy: int, nombre: str):
        self.id = id_proy
        self.nombre = nombre

    def __str__(self):
        return f"ID: {self.id} | Proyecto: {self.nombre}"