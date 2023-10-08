# Ingreso año
year = int(input("Ingrese un año: "))

# Comprobando si es bisiesto
if year % 4 == 0:
    if (year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0)):
        print("Es bisiesto.")
else:
    print("NO es bisiesto.")
