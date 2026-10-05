class Departamento:
    def __init__(self, id_dep: int, nombre: str):
        self.id = id_dep
        self.nombre = nombre

    def __str__(self):
        return f"ID: {self.id} | Departamento: {self.nombre}"
