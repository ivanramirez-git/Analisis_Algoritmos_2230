# Librería para calcular tiempos de ejecución
import time
# Librería para números aleatorios
import random

# Clase arreglo que es hija de list


class arreglo(list):
    # Atributos

    # Insertion Sort
    def insertion_sort(self):
        for i in range(1, len(self)):
            j = i
            while j > 0 and self[j] < self[j - 1]:
                self[j], self[j - 1] = self[j - 1], self[j]
                j -= 1
        return self

    # Quick Sort
    def quick_sort(self):
        self.quick_sort_rec(0, len(self) - 1)
        return self

    def quick_sort_rec(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort_rec(low, pi - 1)
            self.quick_sort_rec(pi + 1, high)
        return self

    def partition(self, low, high):
        pivot = self[high]
        i = low - 1
        for j in range(low, high):
            if self[j] <= pivot:
                i += 1
                self[i], self[j] = self[j], self[i]
        self[i + 1], self[high] = self[high], self[i + 1]
        return i + 1

    # Merge Sort
    def merge_sort(self):
        if len(self) > 1:
            mitad = len(self) // 2
            izq = arreglo(self[:mitad])
            der = arreglo(self[mitad:])
            izq.merge_sort()
            der.merge_sort()
            self.merge(izq, der)
        return self

    def merge(self, izq, der):
        i = j = k = 0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                self[k] = izq[i]
                i += 1
            else:
                self[k] = der[j]
                j += 1
            k += 1
        while i < len(izq):
            self[k] = izq[i]
            i += 1
            k += 1
        while j < len(der):
            self[k] = der[j]
            j += 1
            k += 1
        return self


def obtener_mediana(arreglo):
    # Método para ordenar una lista
    arreglo.sort()
    # Obtener longitud
    longitud = len(arreglo)
    # Obtener el indice de la mitad
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (arreglo[mitad - 1]+arreglo[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = arreglo[mitad]
    return mediana


def obtener_mediana_insertion(arreglo):
    # Método para ordenar una lista
    arreglo.insertion_sort()
    # Obtener longitud
    longitud = len(arreglo)
    # Obtener el indice de la mitad
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (arreglo[mitad - 1]+arreglo[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = arreglo[mitad]
    return mediana


def obtener_mediana_quick(arreglo):
    # Método para ordenar una lista
    arreglo.quick_sort()
    # Obtener longitud
    longitud = len(arreglo)
    # Obtener el indice de la mitad
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (arreglo[mitad - 1]+arreglo[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = arreglo[mitad]
    return mediana


def obtener_mediana_merge(arreglo):
    # Método para ordenar una lista
    arreglo.merge_sort()
    # Obtener longitud
    longitud = len(arreglo)
    # Obtener el indice de la mitad
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (arreglo[mitad - 1]+arreglo[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = arreglo[mitad]
    return mediana


# Casos de prueba
# Configuraciones de prueba
n = [10, 100, 1000, 10000, 100000, 1000000]
indice = 1

# Caso promedio: Tiempos de ejecución de un arreglo aleatorio de n elementos
print("Caso promedio: Tiempos de ejecución de un arreglo aleatorio de n elementos")

# Arreglo de n elementos
arreglo_1 = arreglo(random.sample(range(n[indice]), n[indice]))
arreglo_2 = arreglo(arreglo_1.copy())
arreglo_3 = arreglo(arreglo_1.copy())
arreglo_4 = arreglo(arreglo_1.copy())

# Tiempo de ejecución
tiempos_caso_promedio = []
print("Ordenando arreglos por favor espere...")

# Sort con Insertion Sort
tiempo_0 = time.time()
mediana_2 = obtener_mediana_insertion(arreglo_2)
tiempo_f = time.time()
print('Sort con Insertion Sort: La mediana es %f' % mediana_2)
tiempos_caso_promedio.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort con Quick Sort
tiempo_0 = time.time()
mediana_3 = obtener_mediana_quick(arreglo_3)
tiempo_f = time.time()
print('Sort con Quick Sort: La mediana es %f' % mediana_3)
tiempos_caso_promedio.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort con Merge Sort
tiempo_0 = time.time()
mediana_4 = obtener_mediana_merge(arreglo_4)
tiempo_f = time.time()
print('Sort con Merge Sort: La mediana es %f' % mediana_4)
tiempos_caso_promedio.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort nativo
tiempo_0 = time.time()
mediana_1 = obtener_mediana(arreglo_1)
tiempo_f = time.time()
print('Sort nativo: La mediana es %f' % mediana_1)
tiempos_caso_promedio.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Borrar arreglos
del arreglo_1
del arreglo_2
del arreglo_3
del arreglo_4

print()
# Caso peor: Tiempos de ejecución de un arreglo de n elementos ordenado de forma descendente
print("Caso peor: Tiempos de ejecución de un arreglo de n elementos ordenado de forma descendente")

# Arreglo de n elementos
arreglo_1 = arreglo([])
for i in range(n[indice]):
    arreglo_1.append(n[indice] - i)

arreglo_2 = arreglo(arreglo_1.copy())
arreglo_3 = arreglo(arreglo_1.copy())
arreglo_4 = arreglo(arreglo_1.copy())

# Tiempo de ejecución
tiempos_caso_peor = []
print("Ordenando arreglos por favor espere...")

# Sort con Insertion Sort
tiempo_0 = time.time()
mediana_2 = obtener_mediana_insertion(arreglo_2)
tiempo_f = time.time()
print('Sort con Insertion Sort: La mediana es %f' % mediana_2)
tiempos_caso_peor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort con Quick Sort
tiempo_0 = time.time()
mediana_3 = obtener_mediana_quick(arreglo_3)
tiempo_f = time.time()
print('Sort con Quick Sort: La mediana es %f' % mediana_3)
tiempos_caso_peor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort con Merge Sort
tiempo_0 = time.time()
mediana_4 = obtener_mediana_merge(arreglo_4)
tiempo_f = time.time()
print('Sort con Merge Sort: La mediana es %f' % mediana_4)
tiempos_caso_peor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort nativo
tiempo_0 = time.time()
mediana_1 = obtener_mediana(arreglo_1)
tiempo_f = time.time()
print('Sort nativo: La mediana es %f' % mediana_1)
tiempos_caso_peor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Borrar arreglos
del arreglo_1
del arreglo_2
del arreglo_3
del arreglo_4

print()
# Caso mejor: Tiempos de ejecución de un arreglo de n elementos ordenado de forma ascendente
print("Caso mejor: Tiempos de ejecución de un arreglo de n elementos ordenado de forma ascendente")

# Arreglo de n elementos
arreglo_1 = arreglo([])
for i in range(n[indice]):
    arreglo_1.append(i + 1)

arreglo_2 = arreglo(arreglo_1.copy())
arreglo_3 = arreglo(arreglo_1.copy())
arreglo_4 = arreglo(arreglo_1.copy())

# Tiempo de ejecución
tiempos_caso_mejor = []
print("Ordenando arreglos por favor espere...")

# Sort con Insertion Sort
tiempo_0 = time.time()
mediana_2 = obtener_mediana_insertion(arreglo_2)
tiempo_f = time.time()
print('Sort con Insertion Sort: La mediana es %f' % mediana_2)
tiempos_caso_mejor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort con Quick Sort
tiempo_0 = time.time()
mediana_3 = obtener_mediana_quick(arreglo_3)
tiempo_f = time.time()
print('Sort con Quick Sort: La mediana es %f' % mediana_3)
tiempos_caso_mejor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort con Merge Sort
tiempo_0 = time.time()
mediana_4 = obtener_mediana_merge(arreglo_4)
tiempo_f = time.time()
print('Sort con Merge Sort: La mediana es %f' % mediana_4)
tiempos_caso_mejor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Sort nativo
tiempo_0 = time.time()
mediana_1 = obtener_mediana(arreglo_1)
tiempo_f = time.time()
print('Sort nativo: La mediana es %f' % mediana_1)
tiempos_caso_mejor.append(tiempo_f - tiempo_0)
print('Tiempo de ejecución: %f s' % (tiempo_f - tiempo_0))

# Borrar arreglos
del arreglo_1
del arreglo_2
del arreglo_3
del arreglo_4

print('Fin del programa')
