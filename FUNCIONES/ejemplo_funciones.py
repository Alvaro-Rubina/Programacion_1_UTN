# Funciones a utilizar
from funciones import *

# 
print("------- Bienvenido ------- \n ** A continuacion se le pedirá que ingrese tantos numeros como decida, hasta que ingrese 0.")

num = int(1)
total_sum = 0

# Suma de digitos
while num != 0:
    num = int(input("Numero: "))
    total_sum += num
    if num != 0:
        add_digits(num)

# Suma total
print(f"\n**La suma total de los numeros ingresados es: {total_sum}")
add_digits(total_sum)

