def mostrar_inventario(inventario: dict):
    if not inventario:
        print("Inventario vacio")
        return
    for id_producto, datos in inventario.items():
        print(f"ID: {id_producto}\nNombre: {datos["nombre"]} - Precio: {datos["precio"]} - Cantidad: {datos["cantidad"]}\n")

def buscar_producto(inventario: dict, id_producto:str):
    producto = inventario.get(id_producto)
    if producto:
        print(f"producto {producto} fue encontrado")
    else:
        print(f"el producto {producto} no fue encontrado")

def eliminar_producto(inventario: dict, id_producto:str):
    eliminado = inventario.pop(id_producto, None)
    if eliminado:
        print("el producto fue eliminado\n")
    else:
        print(f"el producto no fue eliminado\n")

def actualizar_stock(inventario: dict, id_producto:str, nueva_cantidad:int):
    if id_producto in inventario:
        inventario[id_producto]["cantidad"] = nueva_cantidad
        print("stock actualizado\n")
    else:
        print(f"el producto no fue encontrado\n")

def limpiar_inventario(inventario: dict):
    inventario.clear
    print("stock en blanco\n")

def main():
    inventario = {
        "P001": {"nombre": "Laptop Lenovo", "precio": 3500.00, "cantidad": 5},
        "P002": {"nombre": "Mouse Logitech", "precio": 150.00, "cantidad": 25},
        "P003": {"nombre": "Teclado Mecánico", "precio": 400.00, "cantidad": 10},
        "P004": {"nombre": "Monitor Samsung", "precio": 1200.00, "cantidad": 7},
        "P005": {"nombre": "Impresora HP", "precio": 900.00, "cantidad": 4},
        "P006": {"nombre": "Silla Ergonómica", "precio": 800.00, "cantidad": 12}
    }
    
    mostrar_inventario(inventario)
    buscar_producto(inventario, "P001")
    buscar_producto(inventario, "P002")
    buscar_producto(inventario, "P003")
    eliminar_producto(inventario, "P003")
    mostrar_inventario(inventario)
    actualizar_stock(inventario,"P001", 50000)
    mostrar_inventario(inventario)
    limpiar_inventario(inventario)
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()