# Indicador de desempeño: Escribe algoritmos que usan la estrategia de programación dinámica
# Ivan Rene Ramirez Castro
# Analisis de Algoritmos

'''

PROBLEMA DE LA MOCHILA
Supón que se tiene un conjunto de n objetos, cada uno de los cuales tienen un peso y un valor asociados a
él. Además, se cuenta con una mochila capaz de soportar ciertas unidades de peso sin que se rompa. Se
desea guardar en la mochila aquellos objetos de forma tal que maximice el valor acumulado de ellos sin que
exceda la capacidad de peso de la mochila. Formalmente:


Sea $S= [obj_1, obj_2, ..., obj_n]$
Sea $p_i$ el peso de cada objeto $i$ y $v_i$ el valor de cada objeto $i$.
Sea $P$ el peso máximo que soporta la mochila.
El problema de la mochila consiste en encontrar un subconjunto $A$ de $S$ tal que:
La sumatoria de los $v_i$ de los objetos de $A$ sea lo maximo posible.
Siempre y cuando, la sumatoria de los $p_i$ de los objetos de $A$ sea menor o igual a $P$.

'''


'''
Algoritmo con programación dinámica

Para la solución de programación dinámica primero se tiene que pensar en forma recursiva, para el
problema de la mochila sería pensar en el último caso, sea A el subconjunto de objetos que maximiza el
valor acumulado en la mochila (solución del problema):

Si A no contiene al objeto n, A es igual a la solución óptima si el problema tuviera solo los primeros
n-1 objetos.

Si A contiene al objeto n, el valor total acumulado de A es igual a $v_n$ más el valor óptimo del
subconjunto formado por los primeros n-1 objetos con la restricción de que el peso de la mochila no
exceda de $P-p_n$ (para respetar el peso del objeto n).

'''


'''

El algoritmo de la mochila con programación dinámica es:
Entrada: vector con los valores y pesos de cada objeto, así como el peso que soporta la mochila.
Salida: el valor máximo que puede guardar la mochila donde la suma de los pesos de los objetos no rompa
la mochila.


'''


'''

1. Inicializar una matriz con la cantidad de objetos+1 de renglones y el peso de la mochila+1 de
columnas.
2. Para i desde 0 hasta la cantidad de objetos
Inicializar con 0 la posición de la matriz en el renglón i columna 0.
3. Para j desde 0 hasta el peso de la mochila
Inicializar con 0 la posición de la matriz en el renglón 0 columna j.
4. Para i desde 1 hasta cantidad de objetos
Para j desde 1 hasta n
¿Es el peso del objeto i mayor que j?
Sí,
Asigna a la matriz en la posición [i][j] lo que tiene la matriz en la
posición [i-1][j].
No,
Asigna a la matriz en la posición [i][j] el máximo de lo que tiene la matriz
en la posición [i-1][j] o lo que contiene la matriz en la posición [i-1]
[j-peso del objeto i]+valor del objeto i.
5. Regresa el contenido de la matriz en la posición [cantidad de objetos][peso de la
mochila].

'''

'''
Objeto1: {peso: 20, valor: 140}
Objeto2: {peso: 10, valor: 60}
Objeto3: {peso: 25, valor: 50}
Mochila: {capacidad: 30}
Solución: {objetos: [Objeto2, Objeto3], valor: 200, peso: 30}
'''


if __name__ == '__main__':
    # Definición de los objetos
    objetos = [
        {'peso': 20, 'valor': 140, 'nombre': 'Objeto1'},
        {'peso': 10, 'valor': 60, 'nombre': 'Objeto2'},
        {'peso': 25, 'valor': 50, 'nombre': 'Objeto3'},
    ]
    # Definición de la mochila
    mochila = {'capacidad': 30}
    # Solución
    solucion = {'objetos': [], 'valor': 0, 'peso': 0}
    # Inicialización de la matriz
    matriz = [[0 for _ in range(mochila['capacidad'] + 1)] for _ in range(len(objetos) + 1)]
    # Algoritmo de la mochila con programación dinámica
    for i in range(1, len(objetos) + 1):
        for j in range(1, mochila['capacidad'] + 1):
            if objetos[i - 1]['peso'] > j:
                matriz[i][j] = matriz[i - 1][j]
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - objetos[i - 1]['peso']] + objetos[i - 1]['valor'])
    # Obtención de la solución
    solucion['valor'] = matriz[len(objetos)][mochila['capacidad']]
    j = mochila['capacidad']
    for i in range(len(objetos), 0, -1):
        if matriz[i][j] != matriz[i - 1][j]:
            solucion['objetos'].append(objetos[i - 1])
            j = j - objetos[i - 1]['peso']
    solucion['objetos'].reverse()
    solucion['peso'] = sum([objeto['peso'] for objeto in solucion['objetos']])
    # Impresión de la solución
    print('Objetos:', objetos)
    print('Mochila:', mochila)
    print('Solución:', solucion)

    # Fin del programa