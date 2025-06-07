#Una clínica desea calcular el Índice de Masa Corporal (IMC) de un paciente, que se obtiene dividiendo el peso por la altura al cuadrado.

#Declaracion y solicitud de datos al paciente
print("\nBienvenido a la calculadora de tu indice de masa corporal!\n")
print("Por favor ingresa los siguientes datos:\n")

peso = float(input("Peso en KG: "))
altura = float(input("Altura en metros: "))

imc = peso / altura**2

print(f"\nGracias por usar nuestra calculadora\nTu indice de masa corporal es de {imc:.2f}")
