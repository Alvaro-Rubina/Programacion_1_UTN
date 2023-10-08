years = int(input("Cuantos años tiene su computadora?: \n"))

if (years >= 0) and (years <=2):
    print("Su computadora es nueva.")
elif (years > 2):
    print("Su computadora es vieja.")
else:
    print("ERROR: No puede ingresar un numero negativo.")