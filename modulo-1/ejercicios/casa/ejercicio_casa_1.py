#Solicita el nombre de un estudiante y su nota final. Muestra si aprobó el curso (nota ≥ 3.0).

nombre = input("\nPor favor escribe tu nombre: ")
nota_final = float(input("digita tu nota final: "))

if(nota_final >= 3 and nota_final <= 5):
    print(f"Felicidades {nombre} aprobaste el curso con una nota final de {nota_final:.2f}")
elif(nota_final < 3 and nota_final > 0):
    print(f"Esta vez no te alcanzo para pasar {nombre} con una nota de {nota_final:.2f} :(, Pero no te desmotives, la siguiente vez seguro lo logras!!!")
else:
    print("ups, parece que ingresaste mal los datos, intenta de nuevo")