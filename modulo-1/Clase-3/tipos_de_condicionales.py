#condicional simple

edad = int(input("ingrese la edad: "))

if edad > 18:
    print("eres mayor de edad")

#condicional compuesta
nota = float(input("ingrese la nota: "))
if nota >= 3:
    print("pasaste")
else:
    print("no pasaste")

#condicional compuesta
nota = float(input("ingrese la nota: "))
if nota >= 3 and nota <= 5:
    print("pasaste")
elif nota >= 0 and nota < 3:
    print("no pasaste")
else:
    print("error")

#condicional anidada
usuario = input("ingrese el usuario: ")
clave = input("ingrese la clave: ")

if usuario == "root":
    if clave == "admin":
        print("bienevenido al home de la app")
    else:
        print("clave incorrecta")
else:
    print("usuario no encontrado")