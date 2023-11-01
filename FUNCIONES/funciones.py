import random
import math

# FUNCIONES PARA EJERCICIOS COMPLEMENTARIOS ------------------------------------------------------------
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

# FUNCIONES DE TP 5 ------------------------------------------------------------------------------

# Funcion verificacion dni (ejercicio 1)
def dni_verification(document):
    if (len(document) == 7) or (len(document) == 8):
        valid = True
    else:
        valid = False
    return valid

# Funcion verificacion largo ultima palabra de un string (ejercicio 2)
def last_word_lenght(w_list):
    last_word = w_list[-1]
    l_w_length = len(last_word)

    return l_w_length

# Funcion para ingresar y verificar nombre del integrante (ejercicio 3)
def name_verification(m_name):
    valid_name = True
    if (len(m_name) < 2) or (len(m_name) > 3):
        valid_name = False
    
    return valid_name

# Funcion para generar el identificador del integrante (ejercicio 3)
def member_id_generator(m_name, dni):
    first_name = str(m_name[0]).replace(',', '').strip().capitalize()
    last_name_length = str(len(m_name[-1]))
    first_numbers_dni = str(dni[0:3])
    member_id = str(first_name + last_name_length + first_numbers_dni)
    return member_id

def is_multiple(a, b):
    if a % b == 0:
        return print('El primer número ingresado es múltiplo del segundo.')
    else:
        return print('El primer número no es múltiplo del segundo')

def avg_temperature(max_temp, min_temp):
    return (max_temp + min_temp) / 2

def return_wh_spaces(a_string):
    new_string = ""
    for character in a_string:
        if character.isalpha():
            new_string += character + " "
        else:
            new_string += character
    return new_string

def mayor_menor(number_list):
    el_mayor = number_list[0]
    el_menor = number_list[0]
    for i in number_list:
        if i > el_mayor:
                el_mayor = i
        if i < el_menor:
                el_menor = number_list[i]
    return "El mayor valor es: " + str(el_mayor) + " el menor valor es: " + str(el_menor)
def circunferencia(radius):
    area = math.pi*(radius ** 2)
    perimeter = 2 * math.pi * radius
    return "El perimeter del radio ingresado es: " + str(perimeter) + " y el area es: " + str(area)

def login(password, user, attempt):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        attempt += 1
        return False


#Numero primo TP5-Ej13    
def vector_magnitude(a,b,c):
    magnitude = math.sqrt(a**2 + b**2 + c**2)
    print(f"La magnitud de un vector que tiene componentes {a,b,c} es {abs(magnitude)}")

#Numero primo TP5-Ej14  
def prime_number(number):
    prime_numb = True
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    
    if count > 2:
        prime_numb = False
    
    return prime_numb

#Factorial TP5-Ej15
def factorial(number):
    factorial = 1    
    for n in range(1, number+1):
        factorial *= n
        
    print(f"El factorial de {number} es {factorial}")
        

#ej 10
def apply_discount(shopping_cart, discounts):
    final_prize= 0
    

    for product, prize in shopping_cart.items():

        if product in discounts:

            discount = discounts[product]
            discount_prize = prize * (1 - discount / 100)
            final_prize += discount_prize

        else:

            final_prize += prize

    return final_prize

#ej 11
def apply_function_to_list(func, input_list):
    result = []
    for element in input_list:
        result.append(func(element))
    return result

#ej 11
def square(x):
    return x ** 2

#ej 12
def word_length_dict(phrase):
    words = phrase.split()
    result = {}

    for word in words:
        result[word] = len(word)

    return result

# FUNCIONES TRABAJO PRACTICO 6 -----------------------------------------------------------------------------
def valid_index(row, column):
    valid = True
    if (row < 0 or row > 3) or (column < 0 or column > 3):
        print("** La posicion ingresada no existe! Intente nuevamente")
        valid = False
    return valid

# FUNCIONES DE TP7 ---------------------------------------------------------------------------------------------

# Función para ordenamiento BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # El último i elementos ya están en su lugar correcto, así que no es necesario revisarlos nuevamente
        for j in range(0, n - i - 1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#Funcion para ordenamiento bubble sort descendente
def bubble_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Función para ordenamiento SELECTION SORT
def selection_sort(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del arreglo
    for i in range(n):
        # Encontrar el valor mínimo en el arreglo sin ordenar
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_index] = arr[min_index], arr[i]

#Funcion para ordenar diccionario mediante metodo de ordenamiento BURBUJA
def bubble_sort_3(dictionary, key):

    n = len(dictionary)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if dictionary[j][key] > dictionary[j + 1][key]:
                dictionary[j], dictionary[j + 1] = dictionary[j + 1], dictionary[j]
    return dictionary

# Función para ordenamiento INSERT SORT
def insertion_sort(arr):
    n = len(arr)

    # Recorremos desde el segundo elemento hasta el último
    for i in range(1, n):
        # Guardamos el valor actual para compararlo e insertarlo en la posición correcta
        current_value = arr[i]
        position = i

        # Movemos los elementos mayores hacia la derecha
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        # Insertamos el valor actual en la posición correcta
        arr[position] = current_value

# Función para ordenamiento MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Fusionar las dos mitades ordenadas
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Función búsqueda lineal
def search_element(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False

def search_element_2(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i  # Se encontró el elemento, devolvemos su índice
    return -1  # El elemento no se encuentra en la lista

# Función búsqueda binaria
def binary_search(array, element):
    left = 0
    right = len(array) - 1

    while left <= right:
        half = (left + right) // 2

        if array[half] == element:
            return half  # Se encontró el elemento, devolvemos su índice
        elif array[half] < element:
            left = half + 1
        else:
            right = half - 1

    return -1  # El elemento no se encuentra en la lista

'''Función COUNT_SORT'''
def count_sort(array):
    # Encuentra el valor máximo en la lista
    maxim = max(array)

    # Crea un arreglo auxiliar para contar las apariciones de cada número
    count = [0] * (maxim + 1)

    # Llena el arreglo de conteo con las apariciones de cada número
    for num in array:
        count[num] += 1

    # Reconstruye la lista ordenada a partir del arreglo de conteo
    array_ord = []
    for i in range(len(count)):
        for j in range(count[i]):
            array_ord.append(i)

    return array_ord

# FUNCIONES DE TP8 ---------------------------------------------------------------------------------------------
def cant_digit(num):

    if num < 10:
        return 1
    else:
        return 1 + cant_digit(num // 10)

def potencia(number1, number2):

    if number1 == number2:
        return True
    elif number1 < number2:
        return False
    else:
        return potencia(number1/ number2, number2)

def find(string1, string2, index=0):
    if index >= len(string1) - len(string2) + 1:
        return []
    if string1[index:index + len(string2)] == string2:
        return [index] + find(string1, string2, index + 1)
    else:
        return find(string1, string2, index + 1)