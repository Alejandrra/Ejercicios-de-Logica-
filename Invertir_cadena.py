""" Crea un programa que invierta el orden de una cadena de texto
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
 """""

def invertir_cadenas(texto):
    resultado = ""  # Inicializamos una cadena vacía 
    for i in range(len(texto) - 1, -1, -1):  # Recorremos el ultimo carcter hasta el primero
        resultado += texto[i]  # Agregamos cada carácter al resultado
    return resultado  # Retornamos la cadena invertida

# Ejemplo de uso
cadena = "Hola mundo"
cadena_invertida = invertir_cadenas(cadena)

# Imprimimos el resultado
print("Cadena original:", cadena)
print("Cadena invertida:", cadena_invertida)
