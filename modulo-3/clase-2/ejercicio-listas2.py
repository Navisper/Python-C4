def agregar_turno(turnos, nombre, dia, turno):
    if not nombre or not dia or not turno:
        raise ValueError("Todos los campos son obligatorios")
    
    turnos.append([nombre.title(), dia.title(), turno.title()])

def insertar_turno(turnos, indice, nombre, dia, turno):
    if not nombre or not dia or not turno:
        raise ValueError("Todos los campos son obligatorios")
    if indice < 0 or indice > len(turnos) :
        raise IndexError("Indice fuera de rango")
    turnos.insert(indice, [nombre.title(), dia.title(), turno.title()])

def eliminar_turno_por_nombre(turnos, nombre):
    for t in turnos:
        if t[0] == nombre.title():
            turnos.remove(t)
            return
    raise ValueError("El empleado no existe")

def eliminar_ultimo_turno(turnos):
    if not turnos:
        raise IndexError("no hay turnos para eliminar")
    return turnos.pop()

def mostrar_turnos(turnos):
    print("\nTurnos asignados:")
    for t in turnos:
        print(f"{t[0]} - {t[1]} - {t[2]}")
    print("\n")

def main():
    turnos = []
    
    try:
        agregar_turno(turnos, "Dayana", "lunes", "Mañana")
        agregar_turno(turnos, "Andres", "miercoles", "noche")
        agregar_turno(turnos, "walter", "jueves", "Mañana")
        agregar_turno(turnos, "alberto", "viernes", "noche")
        agregar_turno(turnos, "Luis", "Sabado", "Dia")
        
        mostrar_turnos(turnos)
        
        insertar_turno(turnos, 1, "Arleys", "martes", "mañana")
        
        mostrar_turnos(turnos)
        
        eliminar_ultimo_turno
        
        mostrar_turnos(turnos)
    
    except (ValueError, IndexError) as e:
        print(e)
    

if __name__ == '__main__':
    main()