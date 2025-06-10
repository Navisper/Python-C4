#Solicita el nombre de una ciudad y la temperatura actual, luego muestra si hace frío (≤18°C), calor (≥30°C) o clima templado.

ciudad = input("Please enter the name of the city: ")

temperatura = float(input("please enter the actual temperature: "))

if(temperatura >= 30):
    print("\nits hot")
elif(temperatura <= 18 ):
    print("\nIts cold")
else:
    print("its warm")