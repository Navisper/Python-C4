biblioteca = {
    "L001": {
        "titulo": "cien años de soledad",
        "autor": "Gabo",
        "año": 1967,
        "disponible":True
    },
    "L002": {
        "titulo": "1984",
        "autor": "George Orwell",
        "año": 1949,
        "disponible":False
    },
    "L003": {
        "titulo": "Don quijote de la mancha",
        "autor": "Miguel de cervantes",
        "año": 1605,
        "disponible":True
    }
}

def mostrar_libro(codigo):
    
    if codigo in biblioteca:
        libro = biblioteca[codigo]
        print(f"\nCodigo: {codigo}")
        print(f"Titulo: {libro["titulo"]}")
        print(f"Autor: {libro["autor"]}")
        print(f"año: {libro["año"]}")
        estado = "disponible" if libro["disponible"] else "no disponible"
        print(estado)
        print("")
    else:
        print(f"el codigo {codigo} no fue encontrado")

mostrar_libro("L002")

def cambiar_disponibilidad(codigo):
    if codigo in biblioteca:
        if biblioteca[codigo]["disponible"]:
            biblioteca[codigo]["disponible"] = False
        else:
            biblioteca[codigo]["disponible"] = True

def cambiar_disponibilidad2(codigo):
    if codigo in biblioteca:
        estado_actual = biblioteca[codigo]["disponible"]
        biblioteca[codigo]["disponible"] = not estado_actual
        nuevo_estado = "disponible" if not estado_actual else "No disponible"
        print(f"El nuevo estado del libro {codigo} es: {nuevo_estado}\n")

cambiar_disponibilidad("L002")
mostrar_libro("L002")
cambiar_disponibilidad2("L002")