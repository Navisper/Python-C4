#Pide el número de participantes en un evento y muestra si se superó el cupo máximo de 100 personas.
participantes = int(input("please enter the number of participants: "))

restante = 100 - participantes

if(restante >= 0):
    print("\nThe limit has not been exceeded")
else:
    print("\nThe limit has been exceeded")