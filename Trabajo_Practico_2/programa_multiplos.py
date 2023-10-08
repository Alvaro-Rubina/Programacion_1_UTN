# Ingreso de los numeros
num1 = int(input("Ingrese el primer numero (Mayor que 0): "))
num2 = int(input("Ingrese el segundo numero (Mayor que 0): "))

# Verifico cual es mayor
if num1 > num2:
    larger = num1
    smaller = num2
elif num2 > num1:
    larger = num2
    smaller = num1

print(" > Mayor: ", larger, "\n > Menor: ", smaller)

# Verifico si el mayor es multiplo del menor

if ((larger <= 0) or (smaller <= 0)):
    print("Por lo menos uno de los numeros ingresados no es valido.")
else:
    if larger % smaller == 0:
        print(larger, " es multiplo de ", smaller)
    else:
        print(larger, " no es multiplo de ", smaller)