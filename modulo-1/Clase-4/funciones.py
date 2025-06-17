def saludar(): #funciones basicas
    print("Hola estudiantes de dev senior en el curso Developer python senior IA")

saludar()

#funciones con parametros
def saludar_estudiante(nombre):
    print(f"hola {nombre} bienvenido a Dev senior")

saludar_estudiante("Julian")

#funciones con retorno de valor
def sumar(num1, num2):
    return num1 + num2

resultado = sumar(10,8)
print(f"la suma es: {resultado}")