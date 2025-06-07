#Pide el nombre de una empresa y el año de fundación, luego muestra cuántos años lleva en funcionamiento.

nombre = input("Digite por favor el nombre de la empresa: ")
año_fundacion = int(input("Por favor ingresa el año de fundacion de la empresa: "))

años_funcionamiento = 2025 - año_fundacion

print(f"\nLa empresa {nombre} lleva en total {años_funcionamiento} años en funcionamiento")