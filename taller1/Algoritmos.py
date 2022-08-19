# Considere la siguiente función recursiva:

# B(1,1)=1
# B(i,1)=B(i−1,i−1) para i>1
# B(i,j)=B(i−1,j−1)+B(i,j−1) para 1<j<=i

# El n-esimo numero de Bell Bn se calcula mediante la función anterior con B(n,n), por ejemplo, para encontrar B3 se debe calcular B(3,3) (De hecho B3=5).

# a) Implemente la función dada mediante un algoritmo.

# Ejemplos
# λ> bell 3 => 5
# λ> map bell [0..10] => [1,1,2,5,15,52,203,877,4140,21147,115975]

import math


def bell_aux(i, j):
    global llamadas
    llamadas += 1
    if i == 1 and j == 1:
        return 1
    elif i > 1 and j == 1:
        return bell_aux(i - 1, i - 1)
    elif 1 < j <= i:
        return bell_aux(i - 1, j - 1) + bell_aux(i, j - 1)
    else:
        return 0


def bell(n):
    return bell_aux(n, n)


# b) Proporcione los números de Bell B1 a B15 y por cada uno presente el numero de llamadas recursivas requeridas para su calculo.
inicio = 1
fin = 12
for i in range(inicio, fin):
    llamadas = 0
    print("Bell B" + str(i) + ": " + str(bell(i)))
    print("Llamadas: " + str(llamadas))
    print("")


# Diseñar un algoritmo iterativo para evaluar n!

def factorial_iterativo(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


for i in range(1, 16):
    print("Factorial de " + str(i) + ": " + str(factorial_iterativo(i)))
    print("")


# Tiempo de ejecución y el modelo de maquina RAM
# Para cada función f(n) y tiempo t de la siguiente tabla, determinar el valor de n de tal manera que el tiempo de ejecución de un algoritmo sea el tiempo t, asumiendo que el mismo algoritmo resuelve el problema en f(n) micro segundos. Por ejemplo, sea f(n)=3^n y t=1 segundo, entonces el valor requerido de n sera igual a 12.5754…

# Cabeceras

cabeceras = ['1 seg', '1 min', '1 hora', '1 dia',
             '1 sema', '1 mes', '1 año', '1 siglo']
func = ['log2(n)', 'sqrt(n)', 'n', 'n^2', 'n^3', '2^n', 'n!']
tabla = []
aux = []


def log2(n):
    return math.log(n, 2)


def sqrt(n):
    return math.sqrt(n)


def n(n):
    return n


def n2(n):
    return n * n


def n3(n):
    return n * n * n


def dos_potencia(n):
    return 2 ** n


def factorial(n):
    return math.factorial(n)

print("Tiempo de ejecución y el modelo de maquina RAM... por favor espere...")
# constantes
segundo = 1
minuto = segundo * 60
hora = minuto * 60
dia = hora * 24
semana = dia * 7
mes = dia * 30
ano = dia * 365
siglo = dia * 365 * 100

# lista de funciones
funciones = [log2, sqrt, n, n2, n3, dos_potencia, factorial]

# lista de tiempos
tiempos = [segundo, minuto, hora, dia, semana, mes, ano, siglo]

# Supongamos que al evaluar n en una función f(n) el resultado nos dal el tiempo de ejecución de la misma.
# 1 seg

# Se recorre la lista de funciones buscando el n que al evaluarlo nos da el tiempo de ejecución mas parecido según el caso
for j in range(len(tiempos)):
    for i in range(len(funciones)):
        n = 1
        while True:
            tiempo = funciones[i](n)
            if tiempo >= tiempos[j]:
                aux.append(n)
                break
            n += 1
            # print('n: ' + str(n) + ' tiempo: ' + str(tiempo))
            if n > 1000000:
                aux.append('>1M')
                break
        # print(' El n para el tiempo ' + cabeceras[j] + ' es ' + str(aux[i]) + ' para la función ' + func[i])

    tabla.append(aux)
    aux = []


# imprimir tabla
print("Tabla de tiempos")
print("Supongamos que disponemos de una maquina donde cada instrucción n se demora 1 segundo")
print("\tCabecera\nTiempo")
for i in range(len(cabeceras)):
    print("\t " + cabeceras[i], end="")

for i in range(len(tabla[0])):
    print("\n" + func[i], end="")
    for j in range(len(tabla)):
        print("\t " + str(tabla[j][i]), end="")
    print("")
print("")
