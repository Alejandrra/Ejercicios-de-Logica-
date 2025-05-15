""""Crea una unica funcion que sea capz de calcular 
    y retornar el area de un poligono.
    la fncion recibira por parametro solo un poligono a la vez.
    Los poligons soportados seran triangulo, cuadrado y rectangulo.
    Imprima el calculo del area de un poligono de cada tipo
 """""""""

def calcula_area(poligono):
    tipo = poligono["tipo"].lower()  # Convertimos a minúscula para evitar errores por mayúsculas

    # Cálculo para triángulo: (base * altura) / 2
    if tipo == "triangulo":
        base = poligono["base"]
        altura = poligono["altura"]
        return (base * altura) / 2

    # Cálculo para cuadrado: lado * lado
    elif tipo == "cuadrado":
        lado = poligono["lado"]
        return lado * lado

    # Cálculo para rectángulo: base * altura
    elif tipo == "rectangulo":
        base = poligono["base"]
        altura = poligono["altura"]
        return base * altura

    else:
        return "Tipo de polígono no soportado"  # muestra mensaje indicandole que el tipo no sporta

# Ejemplos de uso
triangulo = {"tipo": "Triangulo", "base": 20, "altura": 9}
cuadrado = {"tipo": "Cuadrado", "lado": 6}
rectangulo = {"tipo": "Rectangulo", "base": 5, "altura": 5}

# Imprimir el área de cada polígono
print("Área del triángulo:", calcula_area(triangulo))
print("Área del cuadrado:", calcula_area(cuadrado))
print("Área del rectángulo:", calcula_area(rectangulo))
