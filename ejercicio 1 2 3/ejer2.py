# Programa para asignar el grupo A o B

nombre = input("Ingrese su nombre: ").strip().upper()
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ").strip().upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print("Usted pertenece al grupo", grupo)