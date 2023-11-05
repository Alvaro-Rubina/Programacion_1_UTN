# FUNCIONES PARCIAL 2 -----------------------------------------------------------------------------

# Verificacion de gen mutante o humano
def is_mutant(dna):
    mutant = False
    horizontal_sequences = 0
    vertical_sequences = 0
    diagonal_sequences = 0

    # Conteo de secuencias
    horizontal_sequences = horizontal_counting(dna)
    vertical_sequences = vertical_counting(dna)
    diagonal_sequences = diagonal_counting(dna)

    
    # SECUENCIAS TOTALES
    total = horizontal_sequences + vertical_sequences + diagonal_sequences

    # Verificacion si es mutante segun numero de secuencias
    if total > 1:
        mutante = True

    return mutant

# SECUENCIAS HORIZONTALES
def horizontal_counting(dna):
    seqs_counter = 0
    letter_counter = 0

    for row in dna:
        letter_counter = 1
        for letter in range(1, len(row)):
            current_letter = row[letter]
            previous_letter = row[letter - 1]

            # Reviso si hay una secuencia de 1 o mas letras iguales
            if current_letter == previous_letter:
                letter_counter += 1

            # Si se forma una secuencia de letras igual o mayor a 4, sumo 1 al contador de secuencias
            if letter_counter == 4:
                seqs_counter += 1
                break
    
    return seqs_counter



# SECUENCIAS VERTICALES 
def vertical_counting(dna):
    seqs_counter = 0
    letter_counter = 1

    # Recorro cada columna
    for column in range(6):
        letter_counter = 1
        for row in range(1, 6):
            current_letter = dna[row][column]
            previous_letter = dna[row - 1][column]

            if current_letter == previous_letter:
                letter_counter += 1
            else:
                break

            if letter_counter == 4:
                seqs_counter += 1
                break
    
    return seqs_counter

# SECUENCIAS DIAGONALES -----------------------------------------------------------------
def diagonal_counting(dna):
    seqs_counter = 0
    letter_counter = 0

    # SECUENCIAS DESDE IZQUIERDA A DERECHA
    for row in range(3):
        for column in range(3):
            # Defino las letras actuales y siguientes, para luego compararlas
            current_letter = dna[row][column]
            next_letter = dna[row + 1][column + 1]

            if current_letter == next_letter:
                # Si las 2 letras son iguales sumo 2 (ya que tengo ya 2 elementos iguales). Sigo comparando
                letter_counter = 2
                # Verifico de no sobrepasar los indices del array
                while (row + letter_counter < 6) and (column + letter_counter < 6):
                    if dna[row + letter_counter][column + letter_counter] == current_letter:
                        letter_counter += 1
                    else:
                        break

                if letter_counter == 4:
                    seqs_counter += 1


    # SECUENCIAS DESDE DERECHA A IZQUIERDA
    for row in range(3, 6):
        for column in range(3):
            current_letter = dna[row][column]
            next_letter = dna[row - 1][column + 1]

            if current_letter == next_letter:
                letter_counter = 2
                while (row - letter_counter >= 0) and (column + letter_counter < 6):
                    if dna[row - letter_counter][column + letter_counter] == current_letter:
                        letter_counter += 1
                    else:
                        break

                if letter_counter == 4:
                    seqs_counter += 1


    return seqs_counter
