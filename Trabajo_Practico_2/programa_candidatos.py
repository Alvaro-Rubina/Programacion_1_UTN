# Candidatos disponibles
print("Elija un candidato por el cual votar (Ingrese la letra que represente a dicho candidato): ")
print("A) Partido Rojo")
print("B) Partido Verde")
print("C) Partido Azul")

# Eligiendo candidato
choice = input().upper()

if choice == "A":
    print("\nUsted ha votado por el Partido Rojo.")
elif choice == "B":
    print("Usted ha votado por el Partido Verde.")
elif choice == "C":
    print("Usted ha votado por el Partido Azul.")
else:
    print("Opcion erronea; la opcion ingresada no está disponible.")
