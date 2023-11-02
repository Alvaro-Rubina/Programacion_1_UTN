import funciones

# Inicio
print("<<< SISTEMA DE RECLUTAMIENTO DE MUTANTES >>>")
print("** Se comprobara, mediante su ADN, si usted es apto para unirse a la Hermandad y ser parte del combate contra "  
    + "los X-men")

# Ingreso del ADN 
print("\n** Ingrese su secuencia de ADN.")
print("\nIMPORTANTE: Cada secuencia de ADN debe componerse de 6 letras, cuyos valores solo pueden ser [A, T, C, G], " 
    + "representantes de cada base nitrogena del ADN")

# Llenando el array contenedor de las secuencias de ADN
dna = []

for row in range(6):
    while True:
        dna_seq = input(f"- FILA {row + 1} :").upper() 

        # Si el largo de la secuencia es distinto a 6, lo pido nuevamente
        if len(dna_seq) != 6:
            print("La secuencia de ADN debe componerse de 6 letras. Ingreselo nuevamente")
            continue
        else:
            # Verifico que la secuencia de ADN solo contenga las letras permitidas
            valid_seq = True

            for letter in dna_seq:
                # Analizo la letra actual
                valid_letter = letter

                # Si alguna de las letras no es válida, hago un "break" y pido la secuencia de nuevo
                if (valid_letter != 'A' and valid_letter != 'T' and valid_letter != 'C' and valid_letter != 'G'):
                    print("La secuencia de ADN solo debe contener las letras permitidas [A, T, C o G]")
                    valid_seq = False
                    break
            
            # Si la secuencia de ADN cumple todas las condiciones, la agrego a la lista
            if valid_seq:
                dna.append(dna_seq)
                break

# Muestro el ADN ingresado
print("\n** ADN ingresado y procesado correctamente. A continuacion se muestran las secuencias de su ADN **")

for row in dna:
    for letter in row:
        print(letter, end= "  ")
    print()

# Verifico si el ADN es mutante
print("\n----------- RESULTADO DEL ANALISIS -----------")
mutant = funciones.is_mutant(dna)

if mutant:
    print("MUTANTE!: Su ADN contiene mas de 1 secuencia de cuatro letras iguales. Bienvenido a la Hermandad")
else:
    print("HUMANO: Su ADN no contiene secuencias suficientes que verifiquen que usted sea mutante.")