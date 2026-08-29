def separar_pares_impares(lista):
    pares = sorted([x for x in lista if x % 2 == 0])
    impares = sorted([x for x in lista if x % 2 != 0])
    return pares, impares

print(separar_pares_impares([75, 52, 39, 48, 91, 14])) 