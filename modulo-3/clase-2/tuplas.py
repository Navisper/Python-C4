def registrar_empleado(nombre, cargo, salario):
    if not nombre or not cargo or salario <= 0:
        raise ValueError("Datos invalidos")
    return (nombre.title(), cargo.title(), float(salario))

def mostrar_empleados(empleados):
    print("Registro de contratos laborales: ")
    for i, emp in enumerate(empleados, start=1):
        nombre, cargo, salario = emp
        print(f"{i}. {nombre} - {cargo} - {salario:.2f}")

def main():
    empleados = []
    
    try:
        empleados.append(registrar_empleado("ana Garcia", "Ingenieria de software", 8500))
        empleados.append(registrar_empleado("luis perez", "analista de datos", 8000))
        empleados.append(registrar_empleado("juan gonzales", "gerente de servicios", 12000))
        empleados.append(registrar_empleado("Leidy Saenz", "Gerente", 9000))
        empleados.append(registrar_empleado("Jeniffer G", "Diseñadora web", 9500))
        empleados.append(registrar_empleado("Cristian D", "DevOps", 13000))
        empleados.append(registrar_empleado("Jorge J", "Desarrollador web", 10000))
        empleados.append(registrar_empleado("Karol S", "Administradora de base de datos", 15000))
        empleados.append(registrar_empleado("Sergio T", "Scrum master", 11000))
    except ValueError as e:
        print(e)
    
    mostrar_empleados(empleados)

if __name__ == '__main__':
    main()