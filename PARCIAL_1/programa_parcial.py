nombre = input(".-- Bienvenido, ingrese su nombre por favor: ")

eleccion = int(input(f"{nombre}, elija una de las siguientes opciones ingresando su respectivo numero: \n1. Juego de numeros \n2. Juego de palabras \n"))

# Juego segun eleccion del usuario

# JUEGO DE NUMEROS
if eleccion == 1:
    numeros = []
    salida = False

    # Ingreso numeros
    print(f"............... \n{nombre}, Ingrese N numeros enteros. Para dejar de ingresar numeros ingrese 0.")
    
    while salida != True:
        numero = int(input("Numero: "))

        if numero != 0:
            numeros.append(numero)
        else:
            salida = True
            break
    
    # Numeros pares e impares:
    numeros_impares = [num for num in numeros if num % 2 != 0]
    numeros_pares = [num for num in numeros if num % 2 == 0]

    # Salida para numeros pares
    if numeros_pares:
        mayor_numero_par = max(numeros_pares)
        print(f"\nEl mayor número par es: {mayor_numero_par}")
    else:
        print(f"\n{nombre}, no ingresaste números pares.")

    # Salida para numeros impares
    if numeros_impares:
        promedio_impares = sum(numeros_impares) / len(numeros_impares)
        print(f"El promedio de los números impares es: {promedio_impares:.2f}")
    else:
        print(f"{nombre}, no ha ingresado números impares.")

# JUEGO DE PALABRAS
else:
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    frase = input(f"{nombre}, Ingrese una frase: \n")

    for letra in frase:
        if letra in vocales:
            vocales[letra] += 1

    print(f"\n{nombre}, la cantidad de cada vocal en la frase que ha ingresado es de:")
    for vocal, cantidad in vocales.items():
        print(f"{vocal.upper()}: {cantidad}")