''''
* Escribe una función que reciba un texto y retorne verdadero o
* falso (Boolean) según sean o no palíndromos.
* Un Palíndromo es una palabra o expresión que es igual si se lee
* de izquierda a derecha que de derecha a izquierda.
* NO se tienen en cuenta los espacios, signos de puntuación y tildes.
* Ejemplo: Ana lleva al oso la avellana.
'''''''''

import unicodedata
def es_palindromo(texto):
    """
    Esta función recibe un texto y retorna True si es un palíndromo,
    ignorando espacios, signos de puntuación y tildes.
    """
# 1. Convertimos todo el texto a minúsculas para hacer la comparación insensible a mayúsculas
    texto = texto.lower()
# 2. Eliminamos tildes usando normalización Unicode
    texto = ''.join(
    c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn' # 'Mn' son marcas de acento
    )
#3. Eliminamos espacios y signos de puntuación (solo dejamos letras y números)
    texto_filtrado = ''.join(c for c in texto if c.isalnum())

# 4. Comparamos el texto con su versión invertida
    return texto_filtrado == texto_filtrado[::-1]

# Ejemplos de uso
ejemplo1 = "Ana lleva al oso la avellana"
ejemplo2 = "Esto no es un palíndromo"
print(es_palindromo(ejemplo1)) # True
print(es_palindromo(ejemplo2)) # False