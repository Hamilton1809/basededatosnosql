import random
lista_numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", lista_numeros)
lista_numeros.sort()
print("Lista ordenada de menor a mayor:", lista_numeros)