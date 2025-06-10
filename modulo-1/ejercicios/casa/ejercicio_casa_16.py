#Pide el nombre de un cliente y el monto de su compra, luego muestra si aplica a un descuento (si la compra es mayor a $500.000).
nombre_cliente = input("please enter your name: ")
amount = float(input("Please enter the amount of money of your purchase: "))

if (amount > 500000):
    print("\nyou can apply for a discount!!!")
elif(amount <= 500000):
    print("\nWe are sorry, you cant apply for a discount")
else:
    print("error")