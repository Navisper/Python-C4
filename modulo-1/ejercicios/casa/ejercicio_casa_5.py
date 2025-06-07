#Solicita la cantidad de productos vendidos y el precio unitario, luego muestra el total de ventas.

productos_vendidos = int(input("\nDigita la cantidad de productos vendidos: "))
precio_unitario =  float(input("Ingresa por favor el precio unitario de los productos: "))

total_ventas = productos_vendidos * precio_unitario

print(f"\nEl total de ventas fue de {total_ventas:.2f}$")