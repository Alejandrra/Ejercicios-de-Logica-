'''''''''
* Escribe una función que calcule y retorne el factorial de un número dado
* de forma recursiva.
'''''

def factorial(n):

# Caso base: el factorial de 0 o 1 es 1
 if n == 0 or n == 1:
    return 1
 else:
# Llamada recursiva: n! = n * (n-1)!
    return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
