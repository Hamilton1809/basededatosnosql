# Programa para calcular el impuesto según el salario mensual

salario = float(input("Ingrese su salario mensual: "))

if salario >= 12000000 and salario <= 15000000:
    impuesto = salario * 0.03
elif salario > 15000000 and salario <= 20000000:
    impuesto = salario * 0.05
elif salario > 20000000 and salario <= 30000000:
    impuesto = salario * 0.08
elif salario > 30000000:
    impuesto = salario * 0.10
else:
    impuesto = 0

print("El impuesto que debe pagar es: $", impuesto)