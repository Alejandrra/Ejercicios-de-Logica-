""""Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """""""""
 
def son_anagramas(palabra1, palabra2):
    """
    Esta función verifica si dos palabras son anagramas.
    Retorna True si lo son, y False si no.
    """

    # Convertimos ambas palabras a minúsculas para evitar errores por mayúsculas/minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Si las palabras son exactamente iguales, no son anagramas según la condición dada
    if palabra1 == palabra2:
        return False

    # Ordenamos las letras de ambas palabras y las comparamos
    # Si tienen las mismas letras en diferente orden, serán iguales tras ordenar
    return sorted(palabra1) == sorted(palabra2)

# Ejemplos de uso
print(son_anagramas("roma", "amor"))     # True (anagramas)
print(son_anagramas("hola", "hola"))     # False (iguales, no son anagramas)
print(son_anagramas("perro", "gato"))    # False (no son anagramas)
print(son_anagramas("Lento", "NetoL"))   # True (ignora mayúsculas/minúsculas)
