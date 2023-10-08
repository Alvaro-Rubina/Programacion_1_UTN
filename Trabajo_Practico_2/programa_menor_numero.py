# Ingreso numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Verifico el menor
if (num1 < num2) and (num1 < num3):
    print("El primer numero (", num1, ") es el menor de los numeros")
elif (num2 < num1) and (num2 < num3):
    print("El segundo numero (", num2, ") es el menor de los numeros")
else:
    print("El tercer numero (", num3, ") es el menor de los numeros")