def decimalbinario(numero):
    respuesta = ""
    resultado = numero
    while(True):
        valorinicial = resultado 
        residuo = valorinicial % 2
        respuesta += str(residuo)
        resultado = valorinicial // 2
        if resultado == 1:
            respuesta += str(resultado)
            break
    respuesta = "".join(reversed(respuesta))
    return respuesta
numeroentrada = int(input("Ingrese un número para convertir a binario: "))
binario = decimalbinario(numeroentrada)
print("El número decimal", numeroentrada, "en binario es:", binario)