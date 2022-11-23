
# Transcripción del código de Java a Python
def verificarGanador(datos: any):
    # Un jugador puede ganar llenando cualquier fila, columna, diagonales o cuatro esquinas solamente, los numeros que se encuentran en el centro no cuentan
    # los numeros que han salido estan en la lista de numeros
    # id: complejidad temporal, complejidad espacial(si aplica) osea si se esta usando memoria extra
    ganador = False # 1: O(1), O(1)
    # verificar filas
    for i in range(5): # 2: O(5), O(1)
        numerosEncontradosFila = [False] * 5 # 3: O(5), O(5)
        for j in range(5): # 4: O(5), O(1)
            for k in range(datos["indexNumeros"]): # 5: O(5), O(1)
                if datos["tablero"][i][j] == datos["numeros"][k]: # 6: O(1), O(0)
                    numerosEncontradosFila[j] = True # 7: O(1), O(1)
        if numerosEncontradosFila[0] and numerosEncontradosFila[1] and numerosEncontradosFila[2] and numerosEncontradosFila[3] and numerosEncontradosFila[4]: # 8: O(1), O(0)
            ganador = True # 9: O(1), O(1)
            break # 10: O(1), O(0)
    # verificar columnas
    if not ganador: # 11: O(1), O(0)
        for i in range(5):  # 12: O(5), O(1)
            numerosEncontradosColumna = [False] * 5 # 13: O(5), O(5)
            for j in range(5): # 14: O(5), O(1)
                for k in range(datos["indexNumeros"]): # 15: O(5), O(1)
                    if datos["tablero"][j][i] == datos["numeros"][k]: # 16: O(1), O(0)
                        numerosEncontradosColumna[j] = True # 17: O(1), O(1)
            if numerosEncontradosColumna[0] and numerosEncontradosColumna[1] and numerosEncontradosColumna[2] and numerosEncontradosColumna[3] and numerosEncontradosColumna[4]: # 18: O(1), O(0)
                ganador = True # 19: O(1), O(1)
                break # 20: O(1), O(0)
    # verificar diagonales
    if not ganador: # 21: O(1), O(0)
        numerosEncontradosDiagonal1 = [False] * 5 # 22: O(5), O(5)
        numerosEncontradosDiagonal2 = [False] * 5 # 23: O(5), O(5)
        for i in range(5): # 24: O(5), O(1)
            for k in range(datos["indexNumeros"]): # 25: O(5), O(1)
                if datos["tablero"][i][i] == datos["numeros"][k]: # 26: O(1), O(0)
                    numerosEncontradosDiagonal1[i] = True # 27: O(1), O(1)
                if datos["tablero"][i][4 - i] == datos["numeros"][k]: # 28: O(1), O(0)
                    numerosEncontradosDiagonal2[i] = True # 29: O(1), O(1)
        if numerosEncontradosDiagonal1[0] and numerosEncontradosDiagonal1[1] and numerosEncontradosDiagonal1[2] and numerosEncontradosDiagonal1[3] and numerosEncontradosDiagonal1[4]: # 30: O(1), O(0)
            ganador = True # 31: O(1), O(1)
        if numerosEncontradosDiagonal2[0] and numerosEncontradosDiagonal2[1] and numerosEncontradosDiagonal2[2] and numerosEncontradosDiagonal2[3] and numerosEncontradosDiagonal2[4]: # 32: O(1), O(0)
            ganador = True # 33: O(1), O(1)
    # verificar esquinas
    if not ganador: # 34: O(1), O(0)
        numerosEncontradosEsquinas = [False] * 4 # 35: O(4), O(4)
        for i in range(4): # 36: O(4), O(1)
            for k in range(datos["indexNumeros"]): # 37: O(5), O(1)
                if datos["tablero"][0][0] == datos["numeros"][k]: # 38: O(1), O(0)
                    numerosEncontradosEsquinas[0] = True # 39: O(1), O(1)
                if datos["tablero"][0][4] == datos["numeros"][k]: # 40: O(1), O(0)
                    numerosEncontradosEsquinas[1] = True # 41: O(1), O(1)
                if datos["tablero"][4][0] == datos["numeros"][k]: # 42: O(1), O(0)
                    numerosEncontradosEsquinas[2] = True # 43: O(1), O(1)
                if datos["tablero"][4][4] == datos["numeros"][k]: # 44: O(1), O(0)
                    numerosEncontradosEsquinas[3] = True # 45: O(1), O(1)
        if numerosEncontradosEsquinas[0] and numerosEncontradosEsquinas[1] and numerosEncontradosEsquinas[2] and numerosEncontradosEsquinas[3]: # 46: O(1), O(0)
            ganador = True # 47: O(1), O(1)
    if ganador: # 48: O(1), O(0)
        if datos["ganadores"] != None: # 49: O(1), O(0)
            # Agregar a la lista de ganadores
            ganadores = datos["ganadores"] # 50: O(1), O(1)
            # verificar que este tablero no este en la lista de ganadores
            if not datos["id"] in ganadores: # 51: O(1), O(0)
                ganadores.append(datos["id"]) # 52: O(1), O(1)
            datos["ganadores"] = ganadores # 53: O(1), O(1)
        else: # 54: O(1), O(0)
            # Crear la lista de ganadores
            ganadores = [] # 55: O(1), O(1)
            ganadores.append(datos["id"]) # 56: O(1), O(1)
            datos["ganadores"] = ganadores # 57: O(1), O(1)

            

# Analisis de complejidad temporal y espacial de la funcion verificarGanador
# |---------------| Temporal                | Espacial                   |
# |---------------|-------------------------|----------------------------|
# | Identificador | Operacion | Complejidad | Tipo de dato | Espacio     |
# |---------------|-----------|-------------|--------------|-------------|
# | 1             | =         | 1           | bool         | 1           |
# | 2             | for       | 5           | int          | 1           |
# | 3             | =         | 5           | bool         | 5           |
# | 4             | for       | 5           | int          | 1           |
# | 5             | for       | 5           | int          | 1           |
# | 6             | ==        | 1           | bool         | 1           |
# | 7             | =         | 1           | bool         | 1           |
# | 8             | and       | 1           | bool         | 1           |
# | 9             | =         | 1           | bool         | 1           |
# | 10            | break     | 1           | None         | 0           |
# | 11            | not       | 1           | bool         | 1           |
# | 12            | for       | 5           | int          | 1           |
# | 13            | =         | 5           | bool         | 5           |
# | 14            | for       | 5           | int          | 1           |
# | 15            | for       | 5           | int          | 1           |
# | 16            | ==        | 1           | bool         | 1           |
# | 17            | =         | 1           | bool         | 1           |
# | 18            | and       | 1           | bool         | 1           |
# | 19            | =         | 1           | bool         | 1           |
# | 20            | break     | 1           | None         | 0           |
# | 21            | not       | 1           | bool         | 1           |
# | 22            | =         | 5           | bool         | 5           |
# | 23            | =         | 5           | bool         | 5           |
# | 24            | for       | 5           | int          | 1           |
# | 25            | for       | 5           | int          | 1           |
# | 26            | ==        | 1           | bool         | 1           |
# | 27            | =         | 1           | bool         | 1           |
# | 28            | ==        | 1           | bool         | 1           |
# | 29            | =         | 1           | bool         | 1           |
# | 30            | and       | 1           | bool         | 1           |
# | 31            | =         | 1           | bool         | 1           |
# | 32            | and       | 1           | bool         | 1           |
# | 33            | =         | 1           | bool         | 1           |
# | 34            | not       | 1           | bool         | 1           |
# | 35            | =         | 4           | bool         | 4           |
# | 36            | for       | 4           | int          | 1           |
# | 37            | for       | 5           | int          | 1           |
# | 38            | ==        | 1           | bool         | 1           |
# | 39            | =         | 1           | bool         | 1           |
# | 40            | ==        | 1           | bool         | 1           |
# | 41            | =         | 1           | bool         | 1           |
# | 42            | ==        | 1           | bool         | 1           |
# | 43            | =         | 1           | bool         | 1           |
# | 44            | ==        | 1           | bool         | 1           |
# | 45            | =         | 1           | bool         | 1           |
# | 46            | and       | 1           | bool         | 1           |
# | 47            | =         | 1           | bool         | 1           |
# | 48            | if        | 1           | None         | 0           |
# | 49            | !=        | 1           | bool         | 1           |
# | 50            | =         | 1           | list         | 1           |
# | 51            | not       | 1           | bool         | 1           |
# | 52            | append    | 1           | None         | 0           |
# | 53            | =         | 1           | list         | 1           |
# | 54            | else      | 1           | None         | 0           |
# | 55            | =         | 1           | list         | 1           |
# | 56            | append    | 1           | None         | 0           |
# | 57            | =         | 1           | list         | 1           |
# |---------------|-----------|-------------|--------------|-------------|
# | Total         |           | 115         |              | 70          |
# |---------------|-----------|-------------|--------------|-------------|

# Compejidad espacial de los datos de entrada

# Los datos de entrada son un diccionario con 5 claves, donde 3 son enteros, 1 es una lista de listas y 1 es una lista
# Por lo tanto el espacio de los datos de entrada es O(5) = O(1)

# Compejidad espacial de los datos de salida

# Los datos de salida son un diccionario con 6 claves, donde 3 son enteros, 1 es una lista de listas, 1 es una lista y 1 es None o una lista
# Por lo tanto el espacio de los datos de salida es O(6) = O(1)

# Analisis

# Podemos concluir que la complejidad temporal de la funcion verificarGanador no es O(n) ya que no se recorre ninguna lista con un n desconocido
# Por lo tanto la complejidad temporal de la funcion verificarGanador es O(1)

# Podemos concluir que la complejidad espacial de la funcion verificarGanador no es O(n) ya que no se crean espacio de memoria para listas con un n desconocido
# Por lo tanto la complejidad espacial de la funcion verificarGanador es O(1)

# Podemos concluir que la complejidad temporal de la funcion verificarGanador es O(1) y la complejidad espacial de la funcion verificarGanador es O(1) y es un algoritmo eficiente en tiempo y espacio



# Metodo privado para verificar si un numero esta repetido en el tablero
def estaRepetido(numero: int) -> bool:
    # Recorre el arreglo de numeros
    for i in range(5): # 1: O(5), O(1)
        # Recorre el arreglo de numeros
        for j in range(5): # 2: O(5), O(1)
            # Verifica si el numero esta repetido
            if tablero[i][j] == numero: # 3: O(1), O(0)
                return True # 4: O(1), O(1)
    return False # 5: O(1), O(1)

# Analisis de complejidad temporal y espacial de la funcion estaRepetido
# |---------------| Temporal                | Espacial                   |
# |---------------|-------------------------|----------------------------|
# | Identificador | Operacion | Complejidad | Tipo de dato | Espacio     |
# |---------------|-----------|-------------|--------------|-------------|
# | 1             | for       | 5           | int          | 1           |
# | 2             | for       | 5           | int          | 1           |
# | 3             | ==        | 1           | bool         | 1           |
# | 4             | =         | 1           | bool         | 1           |
# | 5             | =         | 1           | bool         | 1           |
# |---------------|-----------|-------------|--------------|-------------|
# | Total         |           | 13          |              | 5           |
# |---------------|-----------|-------------|--------------|-------------|


# Compejidad espacial de los datos de entrada

# Los datos de entrada son un entero
# Por lo tanto el espacio de los datos de entrada es O(1)

# Compejidad espacial de los datos de salida

# Los datos de salida son un booleano
# Por lo tanto el espacio de los datos de salida es O(1)

# Analisis

# Podemos concluir que la complejidad temporal de la funcion estaRepetido es O(1), al ser compuesta por 5 operaciones estaticas

# Podemos concluir que la complejidad espacial de la funcion estaRepetido es O(1), por no crear espacio de memoria variables


import random
# Metodo privado para generar un numero aleatorio
def generarNumeroAleatorio(minimo: int, maximo: int) -> int:
    return random.randint(minimo, maximo) # 1: O(1), O(1)

# Analisis de complejidad temporal y espacial de la funcion generarNumeroAleatorio
# |---------------| Temporal                | Espacial                   |
# |---------------|-------------------------|----------------------------|
# | Identificador | Operacion | Complejidad | Tipo de dato | Espacio     |
# |---------------|-----------|-------------|--------------|-------------|
# | 1             | =         | 1           | int          | 1           |
# |---------------|-----------|-------------|--------------|-------------|
# | Total         |           | 1           |              | 1           |
# |---------------|-----------|-------------|--------------|-------------|

# Compejidad espacial de los datos de entrada

# Los datos de entrada son dos enteros
# Por lo tanto el espacio de los datos de entrada es O(2) = O(1)

# Compejidad espacial de los datos de salida

# Los datos de salida son un entero
# Por lo tanto el espacio de los datos de salida es O(1)

# Analisis

# Podemos concluir que la complejidad temporal de la funcion generarNumeroAleatorio es O(1), al ser compuesta por 1 operacion estatica

# Podemos concluir que la complejidad espacial de la funcion generarNumeroAleatorio es O(1), por no crear espacio de memoria variables

# Metodo privado para generar un tablero
def generarTableroAleatorio(data: any):
    numero: int # 1: O(1), O(1)
    columna: int # 2: O(1), O(1)
    fila: int # 3: O(1), O(1)
    numeros: list[int] = [0] * 25 # 4: O(25), O(25)
    # Genera los numeros aleatorios 
    for i in range(25): # 5: O(25), O(1)
        # Genera un numero aleatorio
        numero = generarNumeroAleatorio(1, 75) # 6: O(funcion), O(1)
        # Verifica que el numero no este repetido
        while estaRepetido(numero): # 7: O(?), O(0)
            numero = generarNumeroAleatorio(1, 75) # 8: O(funcion), O(1)
        # Agrega el numero al arreglo
        numeros[i] = numero # 9: O(1), O(1)
    # Asigna los numeros al tablero
    for i in range(25): # 10: O(25), O(1)
        # Obtiene el numero
        numero = numeros[i] # 11: O(1), O(1)
        # Obtiene la columna
        columna = i % 5 # 12: O(1), O(1)
        # Obtiene la fila
        fila = i // 5 # 13: O(1), O(1)
        # Asigna el numero al tablero
        data[fila][columna] = numero # 14: O(1), O(1)
    # Asigna los numeros a las columnas
    for i in range(5): # 15: O(5), O(1)
        # Obtiene la columna
        columna = i # 16: O(1), O(1)
        # Obtiene el numero minimo
        minimo = (columna * 15) + 1 # 17: O(1), O(1)
        # Obtiene el numero maximo
        maximo = minimo + 14 # 18: O(1), O(1)
        # Asigna los numeros a la columna
        for j in range(5): # 19: O(5), O(1)
            # Obtiene el numero
            numero = data[j][columna] # 20: O(1), O(1)
            # Verifica que el numero este en el rango
            if numero < minimo or numero > maximo: # 21: O(1), O(0)
                # Genera un numero aleatorio
                numero = generarNumeroAleatorio(minimo, maximo) # 22: O(funcion), O(1)
                # Verifica que el numero no este repetido
                while estaRepetido(numero): # 23: O(?), O(0)
                    numero = generarNumeroAleatorio(minimo, maximo) # 24: O(funcion), O(1)
                # Asigna el numero al tablero
                data[j][columna] = numero # 25: O(1), O(1)
    # Asigna el numero 0 a la casilla central
    data[2][2] = 0 # 26: O(1), O(1)
    # this.imprimirTablero();
    # refreshPanel()

# Analisis de complejidad temporal y espacial de la funcion generarTableroAleatorio
# |---------------| Temporal                | Espacial                   |
# |---------------|-------------------------|----------------------------|
# | Identificador | Operacion | Complejidad | Tipo de dato | Espacio     |
# |---------------|-----------|-------------|--------------|-------------|
# | 1             | =         | 1           | int          | 1           |
# | 2             | =         | 1           | int          | 1           |
# | 3             | =         | 1           | int          | 1           |
# | 4             | =         | 1           | list[int]    | 25          |
# | 5             | for       | 25          |              | 1           |
# | 6             | =         | 1           | int          | 1           |
# | 7             | while     | ?           |              | 0           |
# | 8             | =         | 1           | int          | 1           |
# | 9             | =         | 1           | int          | 1           |
# | 10            | for       | 25          |              | 1           |
# | 11            | =         | 1           | int          | 1           |
# | 12            | =         | 1           | int          | 1           |
# | 13            | =         | 1           | int          | 1           |
# | 14            | =         | 1           | int          | 1           |
# | 15            | for       | 5           |              | 1           |
# | 16            | =         | 1           | int          | 1           |
# | 17            | =         | 1           | int          | 1           |
# | 18            | =         | 1           | int          | 1           |
# | 19            | for       | 5           |              | 1           |
# | 20            | =         | 1           | int          | 1           |
# | 21            | if        | 1           |              | 0           |
# | 22            | =         | 1           | int          | 1           |
# | 23            | while     | ?           |              | 0           |
# | 24            | =         | 1           | int          | 1           |
# | 25            | =         | 1           | int          | 1           |
# | 26            | =         | 1           | int          | 1           |
# |---------------|-----------|-------------|--------------|-------------|
# | Total         |           | 80 + ? + ?  |              | 47          |
# |---------------|-----------|-------------|--------------|-------------|

# Compejidad espacial de los datos de entrada

# Los datos de entrada son una matriz de 5x5
# Por lo tanto el espacio de los datos de entrada es O(25) = O(1)

# Compejidad espacial de los datos de salida
# Los datos de salida son una matriz de 5x5
# Por lo tanto el espacio de los datos de salida es O(25) = O(1)

# Analisis

# Podemos concluir que la complejidad temporal de la funcion generarTableroAleatorio es O(80 + ? + ?) = O(?), ya que no tenemos certeza de la complejidad de las funciones estaRepetido y generarNumeroAleatorio ya que es una funcion que nosotros no podemos controlar, en el peor de los casos la complejidad de la funcion estaRepetido es O(n) y la complejidad de la funcion generarNumeroAleatorio es O(1), por lo tanto la complejidad temporal de la funcion generarTableroAleatorio es O(80 + n + 1) = O(n)

# La complejidad espacial de la funcion generarTableroAleatorio es O(47) = O(1), ya que la complejidad espacial de los datos de entrada es O(1) y la complejidad espacial de los datos de salida es O(1)


import time
# Test
if __name__ == "__main__":
    # Test
    datos = { 
        "id": 1,
        "tablero": [
            [4, 16, 43, 54, 65],
            [8, 17, 44, 55, 66],
            [9, 18, 45, 56, 67],
            [10, 19, 46, 57, 68],
            [11, 20, 47, 58, 69]
        ],
        "numeros": [4, 16, 43, 54, 65, 8, 17, 44, 55, 66, 9, 18, 45, 56, 67, 10, 19, 46, 57, 68, 11, 20, 47, 58, 69],
        "indexNumeros": 25,
        "ganadores": None
    }
    # en milisegundos
    start_time = time.time()
    verificarGanador(datos)
    print("--- %s seconds ---" % (time.time() - start_time) + " ms : verificarGanador")
    print(datos)


    # variables globales
    tablero: list[list[int]] = [[0] * 5 for i in range(5)]

    # en milisegundos
    start_time = time.time()
    # Genera el tablero
    generarTableroAleatorio(tablero)
    print("--- %s seconds ---" % (time.time() - start_time) + " ms : generarTableroAleatorio")

    # Imprime el tablero
    for i in range(5):
        for j in range(5):
            print(tablero[i][j], end=" ")
        print()





