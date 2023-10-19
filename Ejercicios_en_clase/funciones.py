# Sumar digitos de un numero
def add_digits(numb):
    total = 0
    actual_numb = 0

    while numb != 0:
        actual_numb = numb % 10 
        numb //= 10
        total += actual_numb

    print(f"Suma total de sus digitos: {total}")

# Ahorcado
def hangman(letters_list, word, name):
    attempts = 5

    while attempts > 0:
        # Muestro la longitud (los espacios) de la palabra a adivinar
        print("\n- COLOR:", end = " ")
        for letter in letters_list:
            print(letter, end=" ")

        # Muestro los intentos que le quedan al usuario
        print(f"\n- INTENTOS : {attempts}")

        # Ingreso una letra y verifico si está en la palabra
        letter = input("\nIngrese una letra: ").lower()
        if letter in word:
            print("Correcto!")
            # Reemplazo el "_" por la letra adivinada para actualizar el tablero
            for i in range(len(word)):
                if word[i] == letter:
                    letters_list[i] = letter
        else:
            print("Incorrecto!")
            attempts -= 1

        # mensaje en caso de haber acertado a todas las letras
        print("-----------------------------------")
        if letters_list == list(word):
            print(f"Felicidades, {name}, adivinaste el color!")
            break

        # Mensaje en caso de no haber acertado a la palabra (quedarse sin intentos)
        if attempts == 0:
            print(f"Mala suerte, {name}, no adivinaste el color ({word})")
    