#declarar variables y pedir datos

ca1 = float(input("Digite la calificacion 1: "))
ca2 = float(input("Digite la calificacion 2: "))
ca3 = float(input("Digite la calificacion 3: "))

promedio = ca1 * 0.3 + ca2 * 0.4 + ca3 * 0.3

#implementar condiciones
if(promedio <3 and promedio >= 0):
    print(f"perdio con una nota de {promedio} ")
elif(promedio >= 3 and promedio <= 5):
    print(f"Pasaste! con un promedio de {promedio}")
else:
    print("error, tu promedio no entra dentro de nuestro sistema")