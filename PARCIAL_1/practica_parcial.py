# Importaciones
import random

""". Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres de largo, el
programa le sumará un signo de exclamación al final, y si no es de 4 caracteres el programa le sumará un
signo de interrogación al final. El programa mostrará después la frase final."""
# Ejercicio 1
"""

phrase = input("Ingrese una palabra o una frase: ")

# Verificacion del largo de la frase

if len(phrase) == 4:
    phrase += "!"
else:
    phrase += "?"

# Imprimiendo la frase resultante
print(phrase)

"""

"""Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que adivinarla letra
por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego."""
# Ejercicio 2
"""

print("---- Bienvenido ----")
print("Ingrese 5 palabras, se elegirá de forma aleatoria una de ellas, y luego usted tendrá que adivinarla letra por letra. \n")

# Ingresando palabras
words = []
for i in range(5):
    words.append(input("- Palabra numero " + str(i + 1) + ":"))

# Eleccion de una palabra aleatoria
random_word = random.choice(words).lower()

# Adivinando palabra
attempt = int(3)
current_position = int(0)
guessed = False

print("** Ingrese la primera letra")
while attempt >= 0:
    letter = input("\n - Letra: ").lower()
    
    # Condicion si la letra ingresada es correcta
    if letter == random_word[current_position]:
        print("Correcto! Siguiente letra")
        current_position += 1
        if current_position == len(random_word):
            print("** Felicidades, ha adivinado la palabra!")
            guessed = True
            break
    # Condicion si la letra ingresada es incorrecta
    else:
        print("** Incorrecto! Intente nuevamente")
        attempt -= 1
        print("(Intentos restantes: " + str(attempt) + ")")

if guessed == False:
    print("\n** Mala suerte! No ha adivinado la palabra.")

"""

"""Escribe un programa que cuente cuántas palabras hay en una cadena de texto ingresada por el usuario"""
# Ejercicio 3
"""

print("--- Bienvenido ----")
text = input("Ingrese una cadena de texto: \n")

words = text.split( )

print(f"La cadena ingresada tiene {len(words)} palabras")

"""

"""Una empresa quiere pagar a sus empleados por la asistencia de lunes a viernes y un adicional por las
horas trabajadas los domingos en tareas especiales."""
""" ✔ El empleado asistió todo el mes, además entre 3 y 5 horas los domingos, adiciona el 3 % del sueldo.
    ✔ Si asistió todo el mes y entre 6 y 10 horas los domingos, adiciona el 10 %.
    ✔ No asistió todo el mes y entre 3 y 10 horas los domingos, adiciona el 2 %. """
# Ejercicio 4
"""
# Ingreso de datos del empleado
name = input("--- Bienvenido \n Ingrese el nombre del empleado:")
pay = float(input(f" [EMPLEADO: {name}] Ingrese el salario del empleado: "))
all_month = input(f" [EMPLEADO: {name}] El empleado ha asistido todo el mes? Responda SI o NO: ").upper()
extra_hours = int(input(f" [EMPLEADO: {name}] Cuantas horas extra ha realizado el empleado los días domingo? Recuerde que el máximo son 10:  "))

# Calculo del salario final
if all_month == "SI":
    # Condicion si ha trabajado todo el mes y ademas entre 3 y 5 horas extra
    if (extra_hours >=3) and (extra_hours <=5):
        final_pay = pay + (pay * 0.03)
    # Condicion si ha trabajado todo el mes y ademas entre 6 y 10 horas extra
    elif (extra_hours >= 6) and (extra_hours <= 10):
        final_pay = pay + (pay * 0.10)

elif all_month == "NO":
    if (extra_hours >= 3) and (extra_hours <= 10):
        final_pay = pay + (pay * 0.02)

# Salario final del empleado

print("---------------------")
print(f"** El salario final del empleado [{name}] este mes será de: {final_pay}")

"""

"""Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si
no que los sume"""
# Ejercicio 5
"""

# Ingreso de los numeros
print("---Bienvenido \n Se le pedirá que ingrese 2 numeros enteros: ")
num1 = int(input(" - Primer numero: "))
num2 = int(input(" - Segundo numero: "))

# Verificando numeros
if num1 == num2:
    total = num1 * num2
    print(f"Los numeros son iguales, se multiplican. Resultado: {total}")
elif num1 > num2:
    total = num1 - num2
    print(f"El primer numero es mayor que el segundo, se restan. Resultado: {total}")
else:
    total = num1 + num2
    print(f"El segundo numero es mayor que el primero, se suman. Resultado: {total}")

"""

"""El ANSES requiere clasificar a las personas que se jubilaran en el año de 2010. Existen tres tipos de
jubilaciones: por edad, por antigüedad joven y por antigüedad adulta."""
"""- Las personas adscritas a la jubilación por edad deben tener 60 años o más y una antigüedad en su
    empleo de menos de 25 años.
    - Las personas adscritas a la jubilación por antigüedad joven deben tener menos de 60 años y una
    antigüedad en su empleo de 25 años o más.
    - Las personas adscritas a la jubilación por antigüedad adulta deben tener 60 años o más y una antigüedad
    en su empleo de 25 años o más."""
"""Determinar en qué tipo de jubilación, quedara adscrita una persona."""
# Ejercicio 6
"""

# Preguntando edad y antigüedad laboral
print("--- Bienvenido al servicio de consulta de jubilaciones de ANSES")
age = int(input(" - Ingrese su edad: "))
labor_seniority = int(input(" - Cuantos años de antigüedad tiene en su empleo?: "))

# Determinando el tipo de jubilacion al que quedará adscripto
print(".......................................")
if (age >= 60) and (labor_seniority < 25):
    print("** Usted puede ser adscrito al tipo de jubilacion: JUBILACION POR EDAD.")
    print("\n--- Gracias por usar el servicio de consulta de jubilaciones de ANSES")
elif (age < 60) and (labor_seniority >= 25):
    print("** Usted puede ser adscrito al tipo de jubilacion: JUBILACION POR ANTIGÜEDAD JOVEN.")
    print("\n--- Gracias por usar el servicio de consulta de jubilaciones de ANSES")
elif (age >= 60) and (labor_seniority > 25):
    print("** Usted puede ser adscrito al tipo de jubilacion: JUBILACION POR ANTIGÜEDAD ADULTA.")
    print("\n--- Gracias por usar el servicio de consulta de jubilaciones de ANSES")
else:
    print("** Usted aún no puede ser adscrito a ningún tipo de jubilación porque no cumple los requisitos.")
    print("\n--- Gracias por usar el servicio de consulta de jubilaciones de ANSES")

"""

"""Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un
porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la siguiente
tabla:"""
"""     Tiempo                                          Utilidad
    Menos de 1 año                                  5 % del salario
    1 año o más y menos de 2 años                   7% del salario
    2 años o más y menos de 5 años                  10% del salario
    5 años o más y menos de 10 años                 15% del salario
    10 años o más                                   20% del salario
    """
# Ejercicio 7
"""

print("--- Bienvenido")

# Ingreso de los datos necesarios
pay = float(input(" - Ingrese su salario anual: "))
seniority = int(input(" - Ingrese la cantidad de años de antigüedad que tiene en la empresa: "))

# Determinando la utilidad correspondiente según la antigüedad del trabajador
if seniority < 1:
    utility = pay * 0.05
elif (seniority >= 1) and (seniority < 2):
    utility = pay * 0.07
elif (seniority >= 2) and (seniority < 5):
    utility = pay * 0.10
elif (seniority >= 5) and (seniority < 10):
    utility = pay * 0.15
elif (seniority >= 10):
    utility = pay * 0.20

# Respuesta
print("...........................")
print(f"La utilidad total que recibe en base a su salario anual y el tiempo de antigüedad en la empresa es de: {utility}")

"""