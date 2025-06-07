#Solicita la cantidad de asistentes a una conferencia y calcula cuántos asientos quedan libres en un auditorio de 120 personas.
ASIENTOS_TOTALES = 120
asistentes = float(input("digite por favor el numero de asistentes a la conferencia: "))

asientos_libres = ASIENTOS_TOTALES - asistentes

print(f"\fEl numero total de asientos libres es de: {asientos_libres:.0f}")