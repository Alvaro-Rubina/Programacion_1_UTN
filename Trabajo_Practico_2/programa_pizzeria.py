# Eleccion pizza
print('\n-- Pizzeria "Bella Napoli" --')

print("\nBienvenido.\nPara ordenar una pizza vegetariana ingrese A.\nPara ordenar una pizza NO vegetariana ingrese B")
pizza = input().upper()

# Ingredientes 
print("\n-INGREDIENTES BASE-")
print(" > Mozzarella \n > Tomate")

print("\nPuede elegir uno de los siguientes ingredientes para agregarle:")

if pizza == "A":                                   # Pizza vegetariana
    print("1) Pimiento \n2) Tofu")
    ingredient = int(input())
    if ingredient == 1:
        ingredient = "Pimiento"
    elif ingredient == 2:
        ingredient = "Tofu"
elif pizza == "B":
    print("1) Peperoni \n2) Jamón \n3) Salmón ")    #Pizza no vegetariana
    ingredient = int(input())
    if ingredient == 1:
        ingredient = "Peperoni"
    elif ingredient == 2:
        ingredient = "Jamón"
    elif ingredient == 3:
        ingredient = "Salmón"

# Salida
print("-------------------------")
if pizza == "A":
    print("PIZZA VEGETARIANA")
    print("Ingredientes:")
    print(" > Mozzarella \n > Tomate \n >", ingredient)
    print("Disfrute su comida!")
elif pizza == "B":
    print("PIZZA NO VEGETARIANA")
    print("Ingredientes:")
    print(" > Mozzarella \n > Tomate \n >", ingredient)
    print("Disfrute su comida!")
