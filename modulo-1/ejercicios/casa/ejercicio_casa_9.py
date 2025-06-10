#Solicita el valor de una factura y calcula el valor con IVA (19%).
valor_factura = float(input("please enter the value of the bill: "))

valor_factura_iva = valor_factura * 1.19

print(f"the value of the bill with iva is of {valor_factura_iva:.2f}$")
