"""""Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 """""""""

def contar_palabra(texto):
        texto = texto.lower()
        signos = ",.;:!?\"'()[]{}¿¡- para evitar errores" #se elimina manualmente
        texto_limpio = ""
        for caracter in texto:
            if caracter not in signos:
                texto_limpio += caracter
        else:
            texto_limpio += " "  # Reemplazamos el signo por un espacio

        palabras = []
        palabra = ""
        for caracter in texto_limpio:
            if caracter != " ":
                palabra += caracter
        else:
            if palabra != "":
                palabras.append(palabra)
                palabra = ""
        if palabra != "":  # Añadimos la última palabra 
            palabras.append(palabra)
    
        # Contamos las palabras en un diccionario
        conteo = {}
        for palabra in palabras:
            if palabra in conteo:
                conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    # Mostramos el resultado
        for palabra, cantidad in conteo.items():
            print(f"{palabra}: {cantidad}")


texto = "Hola Hola Hola Hola Hola HOLA."
contar_palabra(texto)



