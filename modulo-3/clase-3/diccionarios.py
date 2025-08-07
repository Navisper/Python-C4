persona = {
    "nombre": "carlos",
    "clave" : 123456,
    "direccion": "av no seque"
}

cliente = dict(
    nombre="carlos",
    clave = 123456,
    direccion = "av asdkfa"
)

print(cliente["nombre"])
print(cliente.get("clave"))