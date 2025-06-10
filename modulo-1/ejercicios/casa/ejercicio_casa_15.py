#Solicita el número de libros prestados y el número de libros devueltos en una biblioteca, luego muestra cuántos libros quedan prestados.

libros_prestados = int(input("please enter the number of books borrowed: "))
libros_regresados = int(input("please enter the number of books returned: "))

libros_restantes = libros_prestados - libros_regresados

print(f"\nThe number of books that still need to be returned is {libros_restantes}")