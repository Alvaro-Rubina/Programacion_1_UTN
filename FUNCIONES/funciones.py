import random

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


# Bingo
def adding_numbers_to_card(b_card, ):
    f = 1
    numbers = []
    # Itero cada fila dentro del cartón de bingo
    for card in b_card:
        print(f"FILA {f} DEL CARTÓN")
        f += 1
        # Itero n en un rango de 5, me permite ingresar 5 numeros por cartón (0 - 4)
        for n in range(5):
            while True:
                # Ingreso el numero
                number = int(input(f"Numero {n + 1}: "))
                # Si el numero ya ha sido ingresado antes, se pide nuevamente
                if number in numbers:
                    print("El numero ya se ha ingresado, ingrese otro")
                    continue
                # Verifico que el numero esté en el rango permitido
                if (number < 1) or (number > 75):
                    print("* Numero invalido, por favor ingrese un numero entre 1 y 75")
                # Si las condiciones anteriores se cumplen, agrego el numero al cartón
                else:
                    numbers.append(number)
                    card.append(number)  
                    break
    return b_card

def showing_card(b_card):
    for card in b_card:
        print(card) 

def bingo_game(b_card):
    while True:
        # Genero una bolilla aleatoria
        ball = random.randint(1, 75)
        print(f"\n* BOLILLA: {ball}")

        # Recorro el cartón buscando algun numero que coincida con la bolilla
        for card in b_card:
            for i in range(len(card)):
                if card[i] == ball:
                    print("¡Numero encontrado!")
                    card[i] = "X"
                    print("* Sus numeros hasta el momento:")
                    showing_card(b_card)
        # Verifico si se ha logrado BINGO
        bingo_h = horizontal(b_card)
        bingo_v = vertical(b_card)
        bingo_d = diagonal(b_card)

        if (bingo_h == True) or (bingo_v == True) or (bingo_d == True):
            print("------- ¡BINGO! -------")
            break
        input("Pulse una tecla para sacar otra bolilla")

# Condiciones para ganar
def horizontal(b_card):
    win = False
    for card in b_card:
        bingo = True
        for num in card:
            if num != "X":
                bingo = False
                break

        if bingo:
            win = True
            break

    return win

def vertical(b_card):
    win = False
    for num in range(5):
        bingo = True
        for card in b_card:
            if card[num] != "X":
                bingo = False
                break

        if bingo:
            win = True
            break

    return win

def diagonal(b_card):
    win = False

    # Diagonal izquierda a derecha
    bingo = True
    for i in range(5):
        if b_card[i][i] != "X":
            bingo = False
            break
    if bingo:
        win = True

    # Diagonal derecha a izquierda
    if not win:
        bingo = True
        for i in range(5):
            if b_card[i][4 - i] != "X":
                bingo = False
                break
        if bingo:
            win = True

    return win