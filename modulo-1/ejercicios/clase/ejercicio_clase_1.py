#declarar y solicitar variables por consola
#Si solo compra el primer producto debe pagar el 100%
#Si compra dos el 70%
#Y si compra los tres es del 65%
print("\n----------TIENDA-----------")
print("\nIngrese el precio de los productos por favor :)\n")

p1 = float(input("Precio producto 1 : "))
p2 = float(input("Precio producto 2 : "))
p3 = float(input("Precio producto 3 : "))

total_a_pagar = p1 + p2 + p3

total_con_descuento = total_a_pagar * 0.65

print("\nGracias por confiar en nosotros!")
print(f"El total a pagar es de: {total_a_pagar}\nPero como son 3 productos lleva un descuento del 35%\nSu total con descuento es : {total_con_descuento}")