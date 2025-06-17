# Constantes de los programas y precios
PRECIO_DESCUENTO = 1800000
PROGRAMA_1 = "Java de Cero a Senior"
PROGRAMA_2 = "Python con IA Aplicada"
PROGRAMA_3 = "Mobile Senior con IA"

# Variables para ventas e ingresos
ventas_programa1 = 0
ventas_programa2 = 0
ventas_programa3 = 0
ingresos_totales = 0

def mostrar_programas():
    print("\nProgramas disponibles:")
    print(f"1. {PROGRAMA_1} - ${PRECIO_DESCUENTO}")
    print(f"2. {PROGRAMA_2} - ${PRECIO_DESCUENTO}")
    print(f"3. {PROGRAMA_3} - ${PRECIO_DESCUENTO}")

def registrar_venta():
    global ventas_programa1, ventas_programa2, ventas_programa3, ingresos_totales
    
    mostrar_programas()
    programa = input("\nSeleccione el programa (1-3): ")
    
    # Validación de programa
    if programa not in ('1', '2', '3'):
        print("Error: Programa inválido")
        return
    
    # Validación de cantidad
    try:
        cantidad = int(input("Cantidad de estudiantes: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser positiva")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return

    # Actualizar ventas e ingresos
    if programa == '1':
        ventas_programa1 += cantidad
    elif programa == '2':
        ventas_programa2 += cantidad
    elif programa == '3':
        ventas_programa3 += cantidad
    
    ingresos_totales += cantidad * PRECIO_DESCUENTO
    print("¡Venta registrada exitosamente!")

def consultar_ingresos():
    print("\nIngresos acumulados:")
    print(f"- {PROGRAMA_1}: ${ventas_programa1 * PRECIO_DESCUENTO}")
    print(f"- {PROGRAMA_2}: ${ventas_programa2 * PRECIO_DESCUENTO}")
    print(f"- {PROGRAMA_3}: ${ventas_programa3 * PRECIO_DESCUENTO}")

def mostrar_total_dia():
    print(f"\nTotal de ingresos del día: ${ingresos_totales}")

# Menú principal
while True:
    print("\n--- SISTEMA DE VENTAS DEV SENIOR ---")
    print("1. Mostrar programas disponibles")
    print("2. Registrar venta")
    print("3. Consultar ingresos por programa")
    print("4. Mostrar total del día")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        mostrar_programas()
    elif opcion == '2':
        registrar_venta()
    elif opcion == '3':
        consultar_ingresos()
    elif opcion == '4':
        mostrar_total_dia()
    elif opcion == '5':
        print("¡Gracias por usar el sistema!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")