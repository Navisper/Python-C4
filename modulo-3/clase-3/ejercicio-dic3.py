#Crear un dicc con 3 elementos
#Actualizar el segundo
#mostrar todos los values y keys

usuarios = {
    "Jugador1": {
        "nombre": "pedro",
        "dispositivo": "xbox",
        "juego": "valorant"
    },
    "Jugador2": {
        "nombre": "Luis",
        "dispositivo": "pc",
        "juego": "genshin"
    }
}

usuarios["Jugador3"] = {
    "nombre": "Miguel",
    "dispositivo": "tablet",
    "juego": "Osu!"
}

usuarios.update({
    "Jugador2": {
        "nombre": "Carlos",
        "dispositivo": "celular",
        "juego": "genshin"
    }
})

print(f"Datos de los jugadores:\n")

for clave, valor in usuarios.items():
    print(f"Jugador:  {clave}\nDatos - {valor}\n\n")