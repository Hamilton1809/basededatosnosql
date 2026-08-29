dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = []

for dia in dias:
    min_temp = float(input(f"Temp mínima del {dia}: "))
    max_temp = float(input(f"Temp máxima del {dia}: "))
    temperaturas.append({"dia": dia, "min": min_temp, "max": max_temp})

minima_absoluta = min(t["min"] for t in temperaturas)
dias_menor_temp = [t["dia"] for t in temperaturas if t["min"] == minima_absoluta]

print("\n--- Resultados ---")
for t in temperaturas:
    media = (t["min"] + t["max"]) / 2
    print(f"{t['dia']} - Temperatura media: {media:.1f}")

print(f"\nDías con menos temperatura ({minima_absoluta}): {', '.join(dias_menor_temp)}")

busqueda = float(input("\nIngrese una temperatura para buscar: "))
coincidencias = [t["dia"] for t in temperaturas if t["max"] == busqueda]

if coincidencias:
    print(f"Días cuya temperatura máxima coincide: {', '.join(coincidencias)}")
else:
    print("Ningún día coincide con esa temperatura máxima.")