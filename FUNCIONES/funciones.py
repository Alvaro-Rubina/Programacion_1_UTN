# Sumar digitos de un numero
def add_digits(numb):
    total = 0
    actual_numb = 0

    while numb != 0:
        actual_numb = numb % 10 
        numb //= 10
        total += actual_numb

    print(f"Suma total de sus digitos: {total}")
