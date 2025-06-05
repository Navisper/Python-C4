#declaracion y solicitud de datos al estudiante por consola

print("\nBIENVENIDO A CALCULA TU NOTA!!!")
print("\nPor favor ingresa tus notas")

nota_1 = float(input("Por favor digita tu nota numero 1: "))
nota_2 = float(input("Por favor digita tu nota numero 2: "))
nota_3 = float(input("Por favor digita tu nota numero 3: "))

print("\nGracias por digitar tus notas! :)")

nota_final = nota_1 * 0.3 + nota_2 * 0.3 + nota_3 * 0.4

print(f"\n0.o Tu nota final te quedo en : {nota_final}")