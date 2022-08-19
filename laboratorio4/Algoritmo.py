# Algoritmo
import random
# Medidor de tiempos
import time
# Matplotlib
import matplotlib.pyplot as plt
# Numpy
import numpy as np

# Ordenamiento burbuja
def BubbleSort(A, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

# Tabla de tiempos
# Cabecera: No, Descripción, Tiempo inicial (s), Tiempo final (s), Diferencia (s)
tabla_tiempos = [["No", "Descripción", "Tiempo inicial (s)", "Tiempo final (s)", "Diferencia (s)"]]

n_0 = 1000
n_f = 10000
paso = 1000
tabla_tiempos_caso_promedio = []
for i in range(n_0, n_f, paso):
    A = []
    for j in range(i):
        A.append(random.randint(1, n_f))
    time_0 = time.time()
    BubbleSort(A, i)
    time_1 = time.time()
    tabla_tiempos_caso_promedio.append([ time_1 - time_0, i])

# Gráfica de la tabla donde el eje x es el numero de datos y el eje y son los tiempos
plt.plot(tabla_tiempos_caso_promedio[:], tabla_tiempos_caso_promedio[:])
plt.xlabel('Numero de datos')
plt.ylabel('Tiempo (s)')
plt.title('Tiempo de ejecución del algoritmo')
plt.show()


