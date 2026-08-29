def es_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def es_triangulo_rectangulo(a, b, c):
  
    if not es_triangulo(a, b, c):
        return False
    
  
    lados = sorted([a, b, c])
    
    return (lados[0]**2 + lados[1]**2) == lados[2]**2

# Pruebas del programa
print("¿Pueden formar triángulo?:", es_triangulo(3, 4, 5))
print("¿Es triángulo rectángulo?:", es_triangulo_rectangulo(3, 4, 5))