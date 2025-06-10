#Pide el número de empleados de dos sucursales y muestra cuál tiene más personal.
sucursal1 = int(input("Please enter the number of employees: "))
sucursal2 = int(input("Please enter the number of employees: "))

diferencia = sucursal1 - sucursal2

if(diferencia == 0):
    print(f"\nThe number of employees are the same")
elif(diferencia > 0):
    print("The first branch has more employees")
elif(diferencia < 0):
    print("The second branch has more employees")
else:
    print("error")