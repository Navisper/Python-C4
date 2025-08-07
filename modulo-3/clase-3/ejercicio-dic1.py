#Ejercicio para crear un gestor de pacientes
paciente = {
    "nombre": "carlos",
    "especie" : "perro",
    "edad" : 4,
    "vacunado" : True
}

#metodos append, values, items, update, pop, keys

print("\nClaves disponibles en el registro del paciente:\n")

#mostrar claves del diccionario
for clave in paciente.keys():
    print(clave)

#mostrar los valores de cada clave
print("\nValores disponibles en cada clave:\n")

for valor in paciente.values():
    print(valor)

#agregar o actualizar datos

paciente.update({
    "nombre": "pachito",
    123 : "xd"
})


#mostrar todos los pares clave-valor del diccionario
print("\nregistro de informacion del diccionario paciente:\n")
for clave, valor in paciente.items():
    print(f"clave - {clave} valor - {valor}")