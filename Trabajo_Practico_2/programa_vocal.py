# Vocales
vowels = ["a", "e", "i", "o", "u"]
# Ingreso de letra
letter = input("Ingrese una letra: ")

# Comprobando si es vocal
if len(letter) == 1:
    if letter in vowels:
        print("Es vocal.")
    else:
        print("NO es vocal.")
else:
    print("No se puede procesar el dato.")

