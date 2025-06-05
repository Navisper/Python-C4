#declaracion y solicitud de datos de produccion a la fabrica
print("\nQuien produce mas? Edicion fabrica ;)\n")

print("Ingresa por favor la produccion de los turnos \n ")
t1 = float(input("Produccion turno 1 -> "))
t2 = float(input("Produccion turno 2 -> "))

diferencia = t1 - t2

print(f"\nLa diferencia de produccion en tu fabrica es {diferencia}")
print("Si es positivo el turno 1 produjo mas, Si es cero tuvieron igual produccion y si es negativo el 2 produjo mas")
