import funciones

print("--------- BINGO ---------")
print("\nBienvendido, antes de jugar, necesita generar su propio cartón")

# Creacion del carton
bingo_card = [[], [], [], [], []]
numbers = []

# Llenado del cartón
print("** Debe llenar su cartón con 25 numeros, sin repetir ninguno, en un rango de entre 1 a 75 inclusives")
bingo_card = funciones.adding_numbers_to_card(bingo_card)
print("¡Cartón creado!")

# Muestro el cartón
print("\n* Los numeros de su cartón son los siguientes:")
funciones.showing_card(bingo_card)

# Inicio del juego
print("\n          --------- BINGO: INICIO DEL JUEGO ---------")
print("** Comienza el juego: Para ganar, debe completar una linea horizontal, vertical, o diagonal en su cartón **")
funciones.bingo_game(bingo_card)
