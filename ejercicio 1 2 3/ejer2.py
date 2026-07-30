# Programa para determinar el grupo del estudiante

nombre = input("Ingrese su nombre: ").upper()
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ").upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print("Usted pertenece al grupo", grupo)