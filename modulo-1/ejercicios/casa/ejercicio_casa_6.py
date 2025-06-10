#Pide la edad de un usuario y muestra si puede acceder a un sistema restringido para mayores de 21 años.
edad = int(input("please enter your age: "))

if(edad >= 21):
    print("you can access to the restringed system")
else:
    print("you are not allowed to enter to the system")