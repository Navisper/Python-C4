#Solicita el puntaje de dos exámenes y muestra si el estudiante mejoró, empeoró o mantuvo su rendimiento.
exam1 = float(input("please enter the grade of your first exam: "))
exam2 = float(input("please enter the grade of your second exam: "))

if(exam1 > exam2):
    print("\nThe student did not improve")
elif(exam1 == exam2):
    print("\nThe student managed to keep his performance")
elif(exam1 < exam2):
    print("\nThe student did improve")
else:
    print("error! please look at the values you wrote and restar the program")