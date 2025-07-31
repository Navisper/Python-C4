def mostrar_clientes(lista_clientes):
    print("Mis clientes son: ")
    for cliente in lista_clientes:
        print(f"- {cliente}")

def agregar_cliente(lista_clientes, nombre):

# validacion de datos de entrada

    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre.title()}")
    else:
        print("Nombre invalido. El nombre debe tener una logitud mayor a 2 y menor de 50 caracteres")

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50):
        print("Nombre invalido. El nombre debe tener una logitud mayor a 2 y menor de 50 caracteres")
        return
    
    if 0 <= indice < len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente {original} fue modificado con éxito. Nuevo nombre: {nuevo_nombre.title()}")
        
    else:
        print("Indice fuera de rango...")

def main():
    clientes = ["Julian", "Maria"]
    
    while True:
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Modificar cliente")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cliente = input("Ingrese el nombre del cliente: ")
            agregar_cliente(clientes, cliente)
        elif opcion == '2':
            mostrar_clientes(clientes)
        elif opcion == '3':
            cliente_id = int(input("Ingrese el ID del cliente a modificar: "))
            nuevo_cliente = input("Ingrese el nuevo nombre del cliente: ")
            modificar_cliente(clientes, cliente_id, nuevo_cliente)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()