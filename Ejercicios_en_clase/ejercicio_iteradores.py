#EJERCICIO 1:

print("EJERCICIO 1: ")

#Variables
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
members = 5

#Ingresando mensaje
num = int(input("-Ingrese un numero para el corrimiento del encriptamiento del mensaje: \n"))
for  n in range(members):
    message = input("-INGRESE EL MENSAJE A ENCRIPTAR: \n").upper()
    message_index = len(message)
    modified_message = ""
    modified_index = 0
    modified_index = int(modified_index)

    #Creando mensaje encriptado
    for letter in message:
        if letter not in alphabet:
            modified_message += letter

        elif letter in alphabet:
            letter_index = alphabet.index(letter)
            modified_index = (letter_index + num) % 27
            modified_message += alphabet[modified_index]
    print(modified_message)


#EJERCICIO 2:

print("EJERCICIO 2:")

num = 1

while num != 0:
    pair_count = 0
    odd_count = 0

    num = input(".- Ingrese un numero mayor que 0. Para terminar el programa ingrese 0: \n")
    num_int = int(num)

    #Si el numero es positivo
    if num_int > 0:
        for i in num:
            num_int = int(i)

            if num_int % 2 == 0:
                pair_count += 1
            else: 
                odd_count += 1

    #Si el numero es 0 (termina el programa)
    elif num_int == 0:
        print("Programa Finalizado.")
        break
    
    #Si el numero es negativo
    else:
        print("El numero ingresado es negativo, ingrese un numero POSITIVO")
        continue

    print("El numero", num, " tiene: \n ", pair_count, " digitos PARES \n ", odd_count, " digitos IMPARES" )


