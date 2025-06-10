#ciclo - for
#bucle - while
print("for:")
for i in range(1,11):
    print(i)

#for each
print("\nfor each: ")
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)

#while
print("\nWhile: ")
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#ejemplo1
print("\nEjemplo1")

suma = 0
numero = int(input("ingrese el numero a sumar: "))

while numero != 0:
    suma += numero
    numero = int(input("ingrese el numero a sumar: "))

print(f"\nLa suma total es: {suma}\n")

#ejemplo2

saldo=5000

while True:
    print("\n--------MENU---------")
    print("1. ver Saldo")
    print("2. retirar dinero")
    print("3. salir")
    
    option = int (input("->Digita la opcion: "))
    
    if option == 1:
        print(f"tu saldo es de {saldo}$")
    elif option == 2:
        retiro = float(input("\nIngresa por favor la cantidad a retirar: "))
        if saldo >= retiro:
            saldo -= retiro
            print("Has retirado exitosamente!!!")
        else:
            print("ups... Parece que no tienes suficiente dinero para retirar")
    elif option == 3:
        print("\nGracias por usar nuestro servicio")
        break
    else:
        print("Opcion invalidad")
        break