#definir un metodo para agregar clientes a una lista
def agregar_cliente(lista:list, cliente:str):
    lista.append(cliente)
    print(f"Cliente '{cliente}' agregado a la lista.")

#definir un metodo para mostrar los clientes de una lista
def mostrar_clientes(lista):
    if not lista:
        print("No hay clientes en la lista.")
    else:
        print("Clientes en la lista:")
        for i, cliente in enumerate(lista, start=1):
            print(f"{i}. {cliente}")

#definir un metodo modificar un cliente de una lista
def modificar_cliente(lista, cliente_id:int, nuevo_cliente:str):
    if 0 < cliente_id <= len(lista):
        lista[cliente_id - 1] = nuevo_cliente
        print(f"Cliente modificado a '{nuevo_cliente}'.")
    else:
        print("ID de cliente no válido.")


def main():
    clientes = []
    
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

