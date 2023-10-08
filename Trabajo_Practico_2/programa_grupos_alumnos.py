# Ingreso datos
name = input("Ingrese su primer nombre: ")
gender = input(("Ingrese M si es mujer o H si es hombre: ")).upper()

# Verificacion
if (((gender == "M") and (name[0] < "M")) or ((gender == "H") and (name[0] > "N"))):
    print("GRUPO A")
else:
    print("GRUPO B")
