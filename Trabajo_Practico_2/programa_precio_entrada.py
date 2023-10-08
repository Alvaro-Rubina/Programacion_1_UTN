# Ingreso datos
age = int(input("Ingrese su edad: "))

# Verificacion
if age < 4:
    print("Precio de entrada: GRATIS")
elif (age >= 4 and age < 18):
    print("Precio de entrada: $500")
else:
    print("Precio de entrada: $1000")