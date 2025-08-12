from datasets import load_dataset

def cargar_reseñas_amazon(cantidad):
    dataset = load_dataset("amazon_polarity", split=f"train[:{cantidad}]")
    reseñas = {}
    for i, entrada in enumerate(dataset, start=1):
        reseñas[f"r{i:03}"] = {
            "titulo": entrada["title"],
            "contenido": entrada["content"],
            "sentimiento": "positivo" if entrada["label"] == 1 else "Negativo"        
        }
    return reseñas

def mostrar_reseñas(reseñas_dict):
    for id_reseñas, datos in reseñas_dict.items():
        print(f"ID: {id_reseñas}")
        
        for clave, valor in datos.items():
            print(f" {clave.capitalize()}: {valor}")
        print()

def main():
    cantidad = 5
    reseñas_estructuradas = cargar_reseñas_amazon(cantidad)
    mostrar_reseñas(reseñas_estructuradas)

if __name__ == "__main__":
    main()