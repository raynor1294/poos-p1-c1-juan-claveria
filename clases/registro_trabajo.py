class RegistroTrabajo:
    def __init__(self, id_reg: int, id_empleado: int, id_proyecto: int, horas: float):
        self.id = id_reg
        self.id_empleado = id_empleado  # Relación 1 a 0..* con Empleado
        self.id_proyecto = id_proyecto  # Relación 1 a 0..* con Proyecto
        self.horas = horas

    def __str__(self):
        return f"Reg: {self.id} | Emp ID: {self.id_empleado} -> Proy ID: {self.id_proyecto} ({self.horas} hrs)"