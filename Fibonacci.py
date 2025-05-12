""""Escribe un programa que imprima los 50 primeros numeros de la susecion
 * - de Fibonacci empezando 0
 * - La serie Fibonacii se compone por una sucesion de numeros.
 * - La que el siguiente siempre es la suma de los dos anteriores.
 * - 0,1,1,2,3,5,8,13
 """""""""

def fibonacci(n):
    a, b = 0, 1 #inicializa valores de la sucesion empezando por 0

    for _ in range(n):  #devuelve el rango de n valor
        print(a, end=' ')  #imprime el valor con un espacio de linea
        a, b = b, a + b  #a toma el valor de b y b toma el valor de a + b

fibonacci(50)



