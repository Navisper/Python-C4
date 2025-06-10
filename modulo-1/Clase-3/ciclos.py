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

saldo = 5.000

historial = []

clave = "1234"

while True:
    print("\n ----MENU----")
    print("1. Ver Saldo")
    print("2. Retirar Dinero")
    print("3. Depositar Dinero")
    print("4. Ver historial de movimientos")
    print("5. Cambiar clave")
    print("6. Salir")
    
    opcion = int(input("Digite la opcion: "))
    
    if opcion == 1:
        print(f"su saldo actual es: {saldo:.3f}")
    elif opcion == 2:
        monto = float(input("cuanto deseas retirar? "))
        if monto <= saldo:
            saldo -= monto
            historial.append(f"Retiraste {monto:.3f}")
            
            print(f"Retiro exitoso. Saldo restante ${saldo:.3f}")
        else:
            print("Saldo insuficiente")
            
    elif opcion == 3:
        monto = float(input("Cuanto quieres depositar? "))
        if monto > 0:
            saldo += monto 
            historial.append(f"Depositaste {monto:.3f}")
            print(f"Deposito exitoso el nuevo saldo es: {saldo:.3f}")
        else:
            print("No puedes depositar montos negativos")
            
    elif opcion ==4:
        print("Historial")
        if len(historial) == 0:
            print("No tienes movimientos")
        else:
            for movimiento in historial:
                print(movimiento)
        
    elif opcion ==5:
        intento = input("Escribe tu clave actual: ")
        if intento == clave:
            nueva = input("Digita tu nueva clave: ")
            clave = nueva 
            print("Tu clave a sido cambiada con exito ")
            
        else:
            print("Clave incorrecta. ")
    
            
            
    elif opcion == 6:
        print("gracias por usar nuestro sistema: ")
        break
    else:
        print("Opcion invalida")