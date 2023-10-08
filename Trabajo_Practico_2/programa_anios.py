# Ingreso años
current_year = int(input("Ingrese el año actual: "))
year = int(input("Ingrese cualquier otro año: "))

# Verifico diferencia entre años
if year == current_year:
    print("Los años ingresados son los mismos.")
elif (year < current_year):
    print("Han pasado ", (current_year - year), " años desde ", year, " hasta el año actual.")
else:
    print("Faltan ", (year - current_year), " años para llegar a ", current_year, ".")