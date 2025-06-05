'''
if(condicion):
    Intrucciones
else:
    Intrucciones
'''

numero = int(input("digite un numero "))

#tomar decisiones (condicional)
if(numero > 0):
    print(f"el { numero } es positivo")
elif(numero == 0):
    print(f"el {numero} es nulo")
else:
    print(f"el {numero} es negativo")