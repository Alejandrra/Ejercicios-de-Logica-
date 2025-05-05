 #Escribe un programa que se encargue de comprobar si un número es o no primo.
 #Hecho esto, imprime los números primos entre 1 y 100.
def es_primo(numero):
    """
    Función que verifica si un número es primo.
    Retorna True si es primo, False si no lo es.
    """
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  
    return True  

# Imprimir los números primos entre 1 y 100
print("Números primos entre 1 y 100:")
for num in range(1, 101):  # Recorremos del 1 al 100
    if es_primo(num):
        print(num, end=" ")  # Mostramos el número primo en la misma línea
