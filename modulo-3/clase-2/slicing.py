ventas_mensuales = [12000, 5000, 14000,18000,10000,20000,3000,4000]
ventas_t2 = ventas_mensuales[3:6]
print("ventas del t2: ",ventas_t2)
ventas_top = [v for v in ventas_mensuales if v > 13000]
print("ventas sobresalientes: ", ventas_top)