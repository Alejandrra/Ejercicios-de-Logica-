""""Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """""""""
 
def es_anagramas(palabra1, palabra2):
    
    # Convertimos las palabras a minúsculas para evitar errores 
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Si las palabras son exactamente iguales, no son anagramas según la condición dada
    if palabra1 == palabra2:
        return False

    # Ordenamos las letras de ambas palabras y las comparamos
    # Si tienen las mismas letras en diferente orden, serán iguales tras ordenar y seran anagramas
    #por eso se usa el sorted para ordernar las palabras
    return sorted(palabra1) == sorted(palabra2)


print(es_anagramas("roma", "amor"))     
print(es_anagramas("hola", "hola"))     
print(es_anagramas("perro", "gato"))    
