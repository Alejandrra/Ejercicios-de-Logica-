""""Escribe un programa que se encargue de comprobar si un 
    numero es primo o no.
    Hecho esto, imprime los numeros primos entre 1 y 100
 """""""""
def num_primos(n):
    if n <= 1: #menores o igual 1
        return False  

    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    return True  

print(num_primos(999)) #true es primo , false es no primo