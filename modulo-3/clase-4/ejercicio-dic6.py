ventas = [
    ("V001", "Luis Rojas", 350000),
    ("V002", "Ana Torres", 580000),
    ("V003", "Carlos Díaz", 420000)
]

ventasDict = {}

for i in ventas:
    ventasDict.update({
        i[0] :  {"cliente": i[1], "monto" : i[2]}
    })



print(type(ventasDict))
print(ventasDict)