# Indicador de desempeño: Escribe algoritmos que usan la estrategia de programación dinámica

'''
 Implementar un programa que calcule los coeficientes binomiales tomando en cuenta N =
[3,5,7,10,15] y K=[0,...,N], utilizando una función recursiva vs una función que use
programación dinámica. Al final deben generar 5 gráficas como se muestra a continuación: 30
puntos
Explica el comportamiento de la complejidad temporal de acuerdo a las graficas de ambas funciones
'''

import matplotlib.pyplot as plt
import numpy as np
import time



def binomial_dinamico(n, k): # Complejidad O(n*k)
    matriz = [[0 for x in range(k + 1)] for x in range(n + 1)] # O(n*k)
    for i in range(n + 1): # O(n)
        for j in range(min(i, k) + 1): # O(k)
            if j == 0 or j == i: # O(1)
                matriz[i][j] = 1 # O(1)
            else: # O(1)
                matriz[i][j] = matriz[i - 1][j - 1] + matriz[i - 1][j] # O(1)
    return matriz[n][k] # O(1)

def binomial_recursivo(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_recursivo(n - 1, k - 1) + binomial_recursivo(n - 1, k)


def graficar(n, k, fun_recursiva, fun_dinamica):
    # titulo es N = n
    # eje lateral es milisegundos
    # eje horizontal es K
    # linea recursiva es azul
    # linea dinamica es naraja
    # colocar los nombres de las lineas en recuadro arriba a la derecha
    
    x = np.arange(0, k + 1, 1)
    y_recursivo = []
    y_dinamico = []
    for i in x:
        inicio = time.time()
        fun_recursiva(n, i)
        fin = time.time()
        y_recursivo.append((fin - inicio) * 1000)
        inicio = time.time()
        fun_dinamica(n, i)
        fin = time.time()
        y_dinamico.append((fin - inicio) * 1000)
    plt.plot(x, y_recursivo, 'b', label='Recursivo')
    plt.plot(x, y_dinamico, 'orange', label='Dinamico')
    plt.title('N = ' + str(n))
    plt.xlabel('K')
    plt.ylabel('Milisegundos')
    plt.legend(loc='upper left')
    plt.show()




def main():
    # n = [10, 15, 20, 25, 30]
    n = [20]
    # n = [3, 5, 7, 10, 15]
    for i in n:
        graficar(i, i, binomial_recursivo, binomial_dinamico)

    # Test de fiabilidad de las funciones
    print('Binomial Dinamica: ', binomial_dinamico(3, 2))
    print('Binomial Recursiva: ', binomial_recursivo(3, 2))

if __name__ == '__main__':
    main()