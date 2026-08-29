n_palabras = int(input("¿Cuántas palabras desea agregar a la lista? "))
lista = [input(f"Palabra {i+1}: ") for i in range(n_palabras)]
buscar = input("Ingrese la palabra que desea buscar: ")
cantidad = lista.count(buscar)
print(f"La palabra '{buscar}' aparece {cantidad} veces en la lista.")