usuarios = {
    "Usuario1": {
        "nombre": "pedro",
        "telefono": 231564,
        "correo": "correo@mail",
        "roles" : ["admin"]
    },
    "Usuario2": {
        "nombre": "Luis",
        "telefono": 23156564,
        "correo": "luis@mail",
        "roles" : ["Cliente"]
    }
}

usuarios["Usuario3"] = {
    
    "nombre": "Miguel",
    "telefono": 65487,
    "correo": "Miguel@mail",
    "roles" : ["admin", "soporte"]
    
}

print(f"Datos de los usuarios:\n")

for clave, valor in usuarios.items():
    print(f"Usuario:  {clave}\nDatos - {valor}\n\n")

print("\nUsuarios con el rol de admin:\n")

for user_id, datos in usuarios.items():
    if "admin" in datos.get("roles", []):
        print(f"Usuario: {user_id} - Nombre - {datos["nombre"]}")