import sys
sys.path.append("D:/GIT/Proyectos/Programacion_1_UTN/FUNCIONES")
import funciones

"""1. Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse."""
"""new_list = []
number = None
while (True):
    number = int(input("Ingresa un número, ingresa 0 cuando desees salir: "))
    if number == 0:
        break

    else:
        new_list.append(number)
print(new_list)"""
"""2. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar."""
"""number_choose = int(input("Ingrese un número para eliminar en la lista: "))
if number_choose in new_list:
    new_list.remove(number_choose)
    print(new_list)
else:
    print("El número " + str(number_choose) + " no pertenece a la lista.")"""
"""3. Imprimir la sumatoria de todos los números de la lista."""
"""addition = 0
for number in new_list:
    addition = addition + number
print("La suma de los valores de la lista es: " + str(addition))"""
"""4. Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella."""
"""number_for_list = int(input("Ingrese un número: "))
minor_list = []
for number in new_list:
    if number < number_for_list:
        minor_list.append(number)
for number in minor_list:
    print(number)"""

"""5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]"""
"""list_for_tuple = []
for number in new_list:
    numero = new_list.count(number)
    new_tuple = (number,numero)
    list_for_tuple.append(new_tuple)

unique_tuples = []
for number in set(new_list):
    count = new_list.count(number)
    unique_tuples.append((number, count))

print(unique_tuples)"""
"""6. Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, 
solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar 'x'.
a. Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b. Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c. Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""
"""students_primary = []
students_secondary = []
while(True):
    student_p = input("Ingrese el nombre de pila de los estudiantes de nivel primario, cuando quiera salir ingrese X: ")
    if student_p == "x":
        break
    else:
        students_primary.append(student_p)
while(True):
    student_s = input("Ingrese el nombre de pila de los estudiantes de nivel secundario, cuando quiera salir ingrese X: ")
    if student_s == "x":
        break
    else:
        students_secondary.append(student_s)
all_students =students_primary + students_secondary
unique_students = list(set(all_students))
print("Nombres de todos los alumnos de nivel primario y secundario (sin repeticiones):")
print(unique_students)
duplicates = [name for name in unique_students if all_students.count(name) > 1]
print("Nombres que se repiten entre los alumnos de nivel primario y secundario:")
print(duplicates)

unique_primary = list(set(students_primary))
unique_secondary = list(set(students_secondary))
names_unique_to_primary = [name for name in unique_primary if name not in unique_secondary]
print("Nombres de nivel primario que no se repiten en los de nivel secundario:")
print(names_unique_to_primary)

"""
"""9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El juego 
consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales."""
# Ejercicio 9

"""
# Parejas
couples = [
        ["AA", "BB", "CC", "DD"],
        ["FF", "AA", "EE","FF"],
        ["BB", "DD", "EE", "CC"]]
# Cartas
cards = [
        ["㋡", "㋡", "㋡", "㋡"],
        ["㋡", "㋡", "㋡", "㋡"],
        ["㋡", "㋡", "㋡", "㋡"]]

count = 0

print("        ---- Bienvenido a MemoTest ----")
print("** Encuentre las 6 parejas del siguente tablero indicando las respectivas filas y columnas:")
print("** ATENCION: Los indices tanto para fila y columna van desde 0 a 3")
while True:
    # Muestro el estado de las cartas adivinadas (o no)
    print("\n* Estado actual *")
    for row in cards:
        for element in row:
            print(element, end= "  ")
        print()
    
    # Pido las posiciones de las cartas a adivinar
    while True:
        print("\n** PRIMERA CARTA:")
        row_1 = int(input("- Fila: "))
        column_1 = int(input("- Columna: "))
        # Valido que la posicion de la primera carta sea valida
        valid_index = funciones.valid_index(row_1, column_1)

        if valid_index == False:
            continue
        
        while True:
            print("** SEGUNDA CARTA:")
            row_2 = int(input("- Fila: "))
            column_2 = int(input("- Columna: "))
            # Valido que la posicion de la segunda carta sea valida
            valid_index = funciones.valid_index(row_2, column_2)

            if valid_index == False:
                continue
            else:
                break
        break

    # Verifico si se ha acertado
    if (row_1 == row_2) and (column_1 == column_2):
        print("\n** Ha ingresado la misma posicion, intente nuevamente!")
    elif couples[row_1][column_1] == couples[row_2][column_2]:
        # En caso de acertar, "volteo" las cartas adivinadas
        print("\n** ¡Pareja adivinada! **")
        cards[row_1][column_1] = couples[row_1][column_1]
        cards[row_2][column_2] = couples[row_2][column_2]
        # Sumo 1 al contador, que si llega a 6 indica que se han encontrado todas las parejas
        count += 1
    else:
        print("\n** ¡Mala suerte! **")

    if count == 6:
        print("\n **** JUEGO TERMINADO, ¡HA ENCONTRADO TODAS LAS PAREJAS ****")

        # Muestro el resultado final una vez mas

        for row in cards:
            for element in row:
                print(element, end= "  ")
            print()
        break
"""

"""10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
a.	la diagonal principal.
b.	la diagonal inversa."""

"""
# Ejercicio 10

# Matriz:
default_array = [
                ["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]

print("** Matriz con la que se trabajará:")
for row in default_array:
    for element in row:
        print(element, end= "   ")
    print()

# Obteniendo la diagonal principal
print("\n** Elementos de la diagonal principal de la matriz:")
for i in range(3):
    print(default_array[i][i], end= "  ")

# Obteniendo la diagonal inversa
print("\n** Elementos de la diagonal inversa de la matriz:")
for i in range(3):
    print(default_array[i][2 - i], end= "  ")

"""