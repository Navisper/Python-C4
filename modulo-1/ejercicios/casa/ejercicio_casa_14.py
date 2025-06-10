#Pide el nombre de un proyecto y los días estimados de duración, luego muestra cuántas semanas tomará (redondeando hacia arriba).
nombre_proyecto = input("please enter the name of the project: ")
duracion = int(input("please enter the number of days to finish the project: "))

semanas = duracion//7 +1

print(f"\nThe number of weeks dedicated to the project will be around {semanas} weeks")