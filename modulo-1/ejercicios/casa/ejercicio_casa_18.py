#Pide el número de horas trabajadas y la tarifa por hora, luego calcula el salario total.
horas = int(input("please enter the number of hours you worked: "))
tarifa = float(input("please enter the payment per hour: "))

total = horas * tarifa

print(f"\nYour final salary is of {total }$")