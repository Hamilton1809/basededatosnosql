for i in range(1, 6):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    if edad >= 80: fase = "Fase 1"
    elif 70 <= edad < 80: fase = "Fase 2"
    elif 60 <= edad < 70: fase = "Fase 3"
    elif 30 <= edad < 60: fase = "Fase 4"
    elif 18 <= edad < 30: fase = "Fase 5"
    else: fase = "En espera de Autorización"
    print(f"Persona {i} asignada a: {fase}\n")