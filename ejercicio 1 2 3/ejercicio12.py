def contar_palabra_en_texto(texto, palabra):
    """
    Función que cuenta las ocurrencias exactas de una palabra en un texto.
    Convierte todo a minúsculas para evitar errores de sensibilidad (Case Insensitive).
    """
  
    texto_normalizado = texto.lower()
    palabra_normalizada = palabra.lower()
    
    
    lista_palabras = texto_normalizado.split()
    
   
    cantidad_repeticiones = lista_palabras.count(palabra_normalizada)
    
    return cantidad_repeticiones


texto_prueba = "El SENA ofrece el programa ADSO. Estudiar ADSO es clave para el futuro porque el talento de ADSO es muy buscado."
palabra_a_buscar = "ADSO"

resultado = contar_palabra_en_texto(texto_prueba, palabra_a_buscar)

print(f"--- Sistema de Análisis de Texto ---")
print(f"Texto analizado: '{texto_prueba}'")
print(f"La palabra '{palabra_a_buscar}' fue encontrada {resultado} veces.")