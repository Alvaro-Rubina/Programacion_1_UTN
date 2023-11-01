# FUNCIONES NECESARIAS PARA PARCIAL 2 -----------------------------------------------------------------------------

# Funcion que verifica si el ADN es mutante segun el numero de secuencias
def is_mutant(dna):
    # Variables
    mutant = False
    horizontal_sequences = 0
    vertical_sequences = 0
    diagonal_sequences = 0

    # Conteo de secuencias
    # SECUENCIAS HORIZONTALES
    horizontal_sequences = horizontal_counting(dna)
    # SECUENCIAS VERTICALES
    vertical_sequences = vertical_counting(dna)
    # SECUENCIAS DIAGONALES
    diagonal_sequences = diagonal_counting(dna)

    
    # SECUENCIAS TOTALES
    total = horizontal_sequences + vertical_sequences + diagonal_sequences

    # Verifico si es mutante o no dependiendo el numero de secuencias (para caso TRUE, total > 1)
    if total > 1:
        mutante = True

    return mutant

# Funcion que cuenta el numero de SECUENCIAS HORIZONTALES
def horizontal_counting(dna):
    seqs_counter = 0
    letter_counter = 0

    # Recorro las secuencias (filas) de la lista
    for row in dna:
        letter_counter = 1
        # Recorro las letras de cada secuencia (empiezo por la segunda letra, porque comparo con la letra anterior)
        for letter in range(1, len(row)):
            current_letter = row[letter]
            previous_letter = row[letter - 1]
            
            # Reviso si hay una secuencia de 1 o mas letras iguales
            if current_letter == previous_letter:
                letter_counter += 1

            # Si se forma una secuencia de letras igual o mayor a 4, sumo 1 al contador de secuencias
            if letter_counter >= 4:
                seqs_counter += 1
                break
    
    return seqs_counter

# Funcion que cuenta el numero de SECUENCIAS VERTICALES (importante revisar, reparar funcionamiento)
def vertical_counting(dna):
    seqs_counter = 0
    letter_counter = 0

    # Recorro las letras de cada secuencia
    for column in range(len(dna[0])):
        letter_counter = 1
        # Recorro las secuencias (filas) de la lista
        for row in range(1, len(dna)):
            current_letter = dna[row][column]
            previous_letter = dna[row - 1][column]

            # Reviso si hay una secuencia de 1 o mas letras iguales
            if current_letter == previous_letter:
                letter_counter += 1
            else:
                letter_counter = 1

            # Si se forma una secuencia de letras igual o mayor a 4, sumo 1 al contador de secuencias
            if letter_counter >= 4:
                seqs_counter += 1
                break
    
    return seqs_counter