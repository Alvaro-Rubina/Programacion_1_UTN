import sys
sys.path.append("D:/GIT/Proyectos/Programacion_1_UTN/FUNCIONES")
import funciones
import random

# Ejercicio funciones -- AHORCADO 
print("--- Bienvenido al juego del ahorcado ---")
user_name = input("** Ingrese su nombre: ")

# Lista de palabras
words = ["rojo", "azul", "amarillo", "verde", "marron", "violeta", "blanco", "celeste"]

# Partida
play = True
game = int(1)

while play == True:
    print(f"\n------------- ADIVINE EL COLOR -------------")

    # Palabra a adivinar
    random_word = random.choice(words)

    # Palabra oculta
    hidden = ["_" for _ in random_word]

    # Adivinando palabra
    funciones.hangman(hidden, random_word, user_name)

    # Termina ejecucion
    play = False