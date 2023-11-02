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
    letter_counter = 0

    # Recorro cada columna
    for column in range(6):
        letter_counter = 1
        # Recorro las filas
        for row in range(1, len(dna)):
            current_letter = dna[row][column]
            previous_letter = dna[row - 1][column]

            # Reviso si hay una secuencia de 1 o mas letras iguales
            if current_letter == previous_letter:
                letter_counter += 1
            else:
                letter_counter = 1

            # Si se forma una secuencia de letras igual o mayor a 4, sumo 1 al contador de secuencias
            if letter_counter == 4:
                seqs_counter += 1
                break
    
    return seqs_counter



# SECUENCIAS DIAGONALES
def diagonal_counting(dna):
    seqs_counter = 0
    letter_counter = 0

    # Diagonales Izquierda a derecha (SEGUIR REVISANDO, NO RETORNA BIEN ULTIMO CASO DE TESTEO)
    for i in range(len(dna)):
        for j in range(len(dna[i])):
            letter_counter = 1
            current_letter = dna[i][j]

            while i < len(dna) - 1 and j < len(dna[i]) - 1:
                next_letter = dna[i + 1][j + 1]

                if current_letter == next_letter:
                    letter_counter += 1

                    if letter_counter == 4:
                        seqs_counter += 1
                        break

                i += 1
                j += 1

    return seqs_counter