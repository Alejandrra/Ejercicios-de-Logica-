'''
* Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
* y retorne lo siguiente:
* - "X" si han ganado las "X"
* - "O" si han ganado las "O"
* - "Empate" si ha habido un empate
* - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
* O si han ganado los 2.
* Nota: La matriz puede no estar totalmente cubierta.
* Se podría representar con un vacío "", por ejemplo.
'''

def analizar_tablero(tablero):
    # Analiza el estado de un tablero 3x3 de Tic Tac Toe y devuelve:
    # "X" si han ganado las X
    # "O" si han ganado las O
    # "Empate" si nadie ganó y la proporción es válida
    # "Nulo" si hay errores en el número de fichas o ganan ambos

    # Comprobamos que sea una matriz 3x3
    if len(tablero) != 3 or any(len(fila) != 3 for fila in tablero):
        return "Nulo"

    # Contamos la cantidad de X y O
    x_count = sum(celda == "X" for fila in tablero for celda in fila)
    o_count = sum(celda == "O" for fila in tablero for celda in fila)

    # Validamos proporciones posibles
    if abs(x_count - o_count) > 1:
        return "Nulo"

    # Función auxiliar para verificar líneas ganadoras
    def gana(jugador):
        # Filas y columnas
        for i in range(3):
            if all(tablero[i][j] == jugador for j in range(3)):
                return True
            if all(tablero[j][i] == jugador for j in range(3)):
                return True

        # Diagonales
        if all(tablero[i][i] == jugador for i in range(3)):
            return True
        if all(tablero[i][2 - i] == jugador for i in range(3)):
            return True

        return False

    x_gana = gana("X")
    o_gana = gana("O")

    # Si ambos ganan, o gana el que no tiene turno, es inválido
    if x_gana and o_gana:
        return "Nulo"
    if x_gana and x_count < o_count:
        return "Nulo"
    if o_gana and o_count < x_count:
        return "Nulo"

    if x_gana:
        return "X"
    elif o_gana:
        return "O"
    elif x_count + o_count < 9:
        return "Empate"  # Se asume que no importa si está incompleto
    else:
        return "Empate"


# Ejemplo de uso:
tablero = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]
print("Resultado:", analizar_tablero(tablero))
