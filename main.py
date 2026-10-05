from dao import SistemaDAO
from clases.departamento import Departamento
from clases.empleado import Empleado
from clases.proyecto import Proyecto
from clases.registro_trabajo import RegistroTrabajo

def menu():
    dao = SistemaDAO()
    
    # Datos iniciales de prueba
    dao.guardar_departamento(Departamento(1, "Tecnología"))
    dao.guardar_proyecto(Proyecto(100, "Migración Cloud"))

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Registrar Departamento")
        print("2. Registrar Empleado (requiere Departamento)")
        print("3. Registrar Proyecto")
        print("4. Registrar Horas de Trabajo (RegistroTrabajo)")
        print("5. Mostrar todos los datos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_dep = int(input("ID del Departamento: "))
            nombre = input("Nombre del Departamento: ")
            dao.guardar_departamento(Departamento(id_dep, nombre))
            print("¡Departamento guardado con éxito!")

        elif opcion == "2":
            id_emp = int(input("ID del Empleado: "))
            nombre = input("Nombre del Empleado: ")
            id_dep = int(input("ID del Departamento al que pertenece: "))
            
            if dao.buscar_departamento(id_dep):
                dao.guardar_empleado(Empleado(id_emp, nombre, id_dep))
                print("¡Empleado guardado con éxito!")
            else:
                print("Error: El departamento no existe.")

        elif opcion == "3":
            id_proy = int(input("ID del Proyecto: "))
            nombre = input("Nombre del Proyecto: ")
            dao.guardar_proyecto(Proyecto(id_proy, nombre))
            print("¡Proyecto guardado con éxito!")

        elif opcion == "4":
            id_reg = int(input("ID del Registro: "))
            id_emp = int(input("ID del Empleado: "))
            id_proy = int(input("ID del Proyecto: "))
            horas = float(input("Cantidad de horas trabajadas: "))

            if dao.buscar_empleado(id_emp) and dao.buscar_proyecto(id_proy):
                dao.guardar_registro(RegistroTrabajo(id_reg, id_emp, id_proy, horas))
                print("¡Registro de trabajo guardado con éxito!")
            else:
                print("Error: El Empleado o el Proyecto no existen.")

        elif opcion == "5":
            print("\n--- DEPARTAMENTOS ---")
            for d in dao.obtener_departamentos(): print(d)
            print("\n--- EMPLEADOS ---")
            for e in dao.obtener_empleados(): print(e)
            print("\n--- PROYECTOS ---")
            for p in dao.obtener_proyectos(): print(p)
            print("\n--- REGISTROS DE TRABAJO ---")
            for r in dao.obtener_registros(): print(r)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()