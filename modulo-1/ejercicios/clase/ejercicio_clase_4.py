#Una empresa reparte su presupuesto en tres departamentos. Se debe calcular qué porcentaje representa cada uno respecto al total.

#declaracion y solicitud de datos al negocio
dep1 = float(input("por favor digite el presupuesto para el primer departamento: "))
dep2 = float(input("por favor digite el presupuesto para el segundo departamento: "))
dep3 = float(input("por favor digite el presupuesto para el tercer departamento: "))

total_presupuesto = dep1 + dep2 + dep3

porcentaje_dep1 = (dep1/total_presupuesto) * 100
porcentaje_dep2 = (dep2/total_presupuesto) * 100
porcentaje_dep3 = (dep3/total_presupuesto) * 100

print(f"\nEl porcentaje para cada departamento son los siguientes:\ndepartamento 1: {porcentaje_dep1:.2f}\ndepartamento 2: {porcentaje_dep2:.2f}\ndepartamento 3: {porcentaje_dep3:.2f}")