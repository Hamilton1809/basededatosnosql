tipo = input("¿Desea una pizza vegetariana? (si/no): ").lower()
print("Ingredientes base: Mozzarella y Tomate")

if tipo == "si":
    print("Ingredientes disponibles: 1. Pimiento 2. Tofu")
    ingrediente = input("Elija un ingrediente (escriba el nombre): ")
    print(f"Su pizza ES vegetariana. Ingredientes: Mozzarella, Tomate y {ingrediente.capitalize()}.")
else:
    print("Ingredientes disponibles: 1. Peperoni 2. Jamón 3. Salmón")
    ingrediente = input("Elija un ingrediente (escriba el nombre): ")
    print(f"Su pizza NO es vegetariana. Ingredientes: Mozzarella, Tomate y {ingrediente.capitalize()}.")