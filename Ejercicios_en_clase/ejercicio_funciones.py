import random


# Ejercicio funciones -- AHORCADO 
print("--- Bienvenido al juego del ahorcado ---")
user_name = input("** Ingrese su nombre : ")

# Lista de palabras
words = ["rojo", "azul", "amarillo", "verde", "blanco", "negro", "violeta", "negro"]

# Partida
play = True
game = int(1)

while play == True:
    print(f"--- Partida {game} ---")

    # Palabra a adivinar
    random_word = random.choice(words)
    word_list = []
    for letter in random_word:
        word_list.append[letter]

    # Adivinando palabra
    
