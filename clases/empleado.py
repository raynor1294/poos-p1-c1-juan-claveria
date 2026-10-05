class Empleado:
    def __init__(self, id_emp: int, nombre: str, id_departamento: int):
        self.id = id_emp
        self.nombre = nombre
        self.id_departamento = id_departamento  # Relación 1 a 0..* con Departamento

    def __str__(self):
        return f"ID: {self.id} | Empleado: {self.nombre} | Dep. ID: {self.id_departamento}"