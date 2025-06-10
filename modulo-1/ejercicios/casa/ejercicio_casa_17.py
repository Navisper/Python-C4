#Solicita la cantidad de materias inscritas por un estudiante y muestra si tiene sobrecarga académica (más de 7 materias).
materias = int(input("please enter the number of classes the student signed: "))

if(materias > 7):
    print("\nThe student has an overchargue of classes")
elif(materias <= 7 and materias > 0):
    print("\nThe student is alright")
else:
    print("error")