'''''''''
* Crea una función que reciba un String de cualquier tipo y se encargue de
* poner en mayúscula la primera letra de cada palabra.
* - No se pueden utilizar operaciones del lenguaje que
* lo resuelvan directamente.
'''''''''

def capitalizar_palabras(texto):
    """
    Toma un texto y convierte la primera letra de cada palabra en mayúscula
    sin usar métodos propios como .title() o .capitalize().
    """
    resultado = "" # Acumulador del resultado final
    nueva_palabra = True # Indicador para saber si estamos al inicio de una palabra
    
    for caracter in texto:
     if caracter == " ":
        # Si encontramos un espacio, la siguiente letra será el inicio de una palab     ra
        resultado += caracter
        nueva_palabra = True
     else:
         if nueva_palabra:
            # Si es el comienzo de una palabra, convertimos el carácter a mayúscula
            if 'a' <= caracter <= 'z': # solo convertimos si es una letra minúscula
               resultado += chr(ord(caracter) - 32)
            else:
                 resultado += caracter
            nueva_palabra = False
         else:
            # Si no es comienzo, agregamos el carácter tal
            resultado += caracter
    return resultado

# Ejemplo
texto = "hola mundo desde python"
print(capitalizar_palabras(texto)) # "Hola Mundo Desde Python"