import sys
sys.path.append("D:/GIT/Proyectos/Programacion_1_UTN/FUNCIONES")
import funciones

"""1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene."""
# Ejercicio 1


number = int(input("* Ingrese un numero: "))

digitos = funciones.cant_digit(number)

print("** La cantidad de digitos del numero ingresado es de: ", digitos)


"""2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b."""
# Ejercicio 2

"""
num1 = int(input("* Ingrese el primer numero: "))
num2 = int(input("* Ingrese el segundo numero: "))

if funciones.potencia(num1, num2):
    print(f"El numero {num1} es potencia de {num2}")
else:
    print(f"El numero {num1} no es potencia de {num2}")
"""

"""3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con 
las posiciones en donde se encuentra b dentro de a"""
# Ejercicio 3

string1 = input("* Ingrese el primer string: ").lower()
string2 = input("* Ingrese el segundo string: ").lower()
positions = funciones.find(string1, string2)


print(f"Las posiciones donde '{string2}' aparece en '{string1}' son: {positions}")