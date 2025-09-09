import os

ARCHIVO_PRODUCTOS = 'productos.txt'

if not os.path.exists(ARCHIVO_PRODUCTOS):
    with open(ARCHIVO_PRODUCTOS, 'w') as f:
        f.write('')

def leer_productos():
    with open(ARCHIVO_PRODUCTOS, 'r') as f:
        lineas = f.readlines()
    productos = []
    for linea in lineas:
        codigo, nombre, precio = linea.strip().split(',')
        productos.append({
            'codigoUnico': codigo,
            'nombre': nombre,
            'precio': float(precio)
        })
    return productos

def guardar_producto(producto):
    with open(ARCHIVO_PRODUCTOS, 'a') as f:
        f.write(f"{producto['codigoUnico']},{producto['nombre']},{producto['precio']}\n")

def mostrar_productos():
    return leer_productos()

def agregar_producto(producto):
    productos = leer_productos()
    if any(p['codigoUnico'] == producto['codigoUnico'] for p in productos):
        raise ValueError("Producto con este código ya existe")
    guardar_producto(producto)
    return producto

def vender_producto(codigo):
    productos = leer_productos()
    for producto in productos:
        if producto['codigoUnico'] == codigo:
            productos.remove(producto)
            with open(ARCHIVO_PRODUCTOS, 'w') as f:
                for p in productos:
                    f.write(f"{p['codigoUnico']},{p['nombre']},{p['precio']}\n")
            return producto
    raise ValueError("Producto no encontrado")

def menu():
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Vender producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    while True:
        opcion = menu()
        if opcion == '1':
            productos = mostrar_productos()
            for producto in productos:
                print(f"Código: {producto['codigoUnico']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}")
        elif opcion == '2':
            codigo = input("Ingrese código único: ")
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio del producto: "))
            try:
                nuevo_producto = agregar_producto({'codigoUnico': codigo, 'nombre': nombre, 'precio': precio})
                print(f"Producto agregado: {nuevo_producto}")
            except ValueError as e:
                print(e)
        elif opcion == '3':
            codigo = input("Ingrese código único del producto a vender: ")
            try:
                vendido = vender_producto(codigo)
                print(f"Producto vendido: {vendido}")
            except ValueError as e:
                print(e)
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()