# Programa para calcular el precio de la entrada

edad = int(input("Ingrese la edad del cliente: "))

if edad < 5:
    precio = 0
elif edad <= 18:
    precio = 5000
else:
    precio = 10000

print("El precio de la entrada es: $", precio)