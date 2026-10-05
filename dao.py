from clases.departamento import Departamento
from clases.empleado import Empleado
from clases.proyecto import Proyecto
from clases.registro_trabajo import RegistroTrabajo


class SistemaDAO:
    """Clase DAO centralizada utilizando almacenamiento en memoria para simplificar."""
    def __init__(self):
        self._departamentos = {}
        self._empleados = {}
        self._proyectos = {}
        self._registros = {}

    # --- Métodos para Departamento ---
    def guardar_departamento(self, dep: Departamento):
        self._departamentos[dep.id] = dep

    def obtener_departamentos(self):
        return list(self._departamentos.values())

    def buscar_departamento(self, id_dep: int):
        return self._departamentos.get(id_dep)

    # --- Métodos para Empleado ---
    def guardar_empleado(self, emp: Empleado):
        self._empleados[emp.id] = emp

    def obtener_empleados(self):
        return list(self._empleados.values())

    def buscar_empleado(self, id_emp: int):
        return self._empleados.get(id_emp)

    # --- Métodos para Proyecto ---
    def guardar_proyecto(self, proy: Proyecto):
        self._proyectos[proy.id] = proy

    def obtener_proyectos(self):
        return list(self._proyectos.values())

    def buscar_proyecto(self, id_proy: int):
        return self._proyectos.get(id_proy)

    # --- Métodos para RegistroTrabajo ---
    def guardar_registro(self, reg: RegistroTrabajo):
        self._registros[reg.id] = reg

    def obtener_registros(self):
        return list(self._registros.values())