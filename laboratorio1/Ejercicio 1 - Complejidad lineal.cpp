#include <iostream>
#include <time.h>
#include <vector>
#include <string>
#include "LibImpresion.h"

// Funcion para calcular la suma de n numeros de forma lineal
long long int suma_lineal(int n)
{
    long long int suma = 0;
    for (int i = 0; i <= n; i++)
    {
        suma += i;
    }
    return suma;
}

// funcion de suma de n numeros de forma constante o gausiana
long long int suma_gausiana(int n)
{
    return (n * (n + ((long long int)1))) / ((long long int)2);
}
// funcion principal calculando el tiempo en segundos de la suma de n numeros de forma lineal
int main()
{
    vector<double> tiempos_lineal;             // tiempo inicial y final en segundos
    vector<double> tiempos_gausiana;           // tiempo inicial y final en segundos
    vector<long long int> ns;                  // vector que contiene los ns a sumar
    vector<long long int> resultados_lineal;   // vector que contiene los resultados de la suma de los ns
    vector<long long int> resultados_gausiana; // vector que contiene los resultados de la suma de los ns

    ns.push_back(1000000);
    ns.push_back(10000000);
    ns.push_back(100000000);
    ns.push_back(1000000000);
    double t_gausiana;
    double t_lineal;
    clock_t t_ini;
    clock_t t_fin;
    for (int i = 0; i < 4; i++)
    {
        cout << "Calculando tiempos de suma de " << ns[i] << " numeros..." << endl;
        // calculando el tiempo de suma de n numeros de forma lineal de ns[0]
        clock_t t_ini = clock();
        resultados_lineal.push_back(suma_lineal(ns[i]));
        clock_t t_fin = clock();
        t_lineal = (double)(t_fin - t_ini) / CLOCKS_PER_SEC;
        tiempos_lineal.push_back(t_lineal);

        // calculando el tiempo de suma de n numeros de forma gausiana de ns[0]
        t_ini = clock();
        resultados_gausiana.push_back(suma_gausiana(ns[i]));
        t_fin = clock();
        t_gausiana = (double)(t_fin - t_ini) / CLOCKS_PER_SEC;
        tiempos_gausiana.push_back(t_gausiana);
    }
    // cabeceras
    // "Datos de entrada\t tiempo suma_lineal\t tiempo suma_constante\t resultado_lineal\t resultado_constante"
    cout << campoMedio(25, ' ', "Datos de Entrada", ROJO) << "\t" << campoMedio(25, ' ', "Tiempo suma_lineal", AZUL) << "\t" << campoMedio(25, ' ', "Tiempo suma_gausiana", AZUL) << "\t" << campoMedio(25, ' ', "Resultado suma_lineal", AZUL) << "\t" << campoMedio(25, ' ', "Resultado suma_gausiana", AZUL) << endl;

    for (int i = 0; i < 4; i++)
    {
        cout << campoMedio(25, ' ', to_string(ns[i]), ROJO) << "\t" << campoMedio(25, ' ', to_string(tiempos_lineal[i]), AZUL) << "\t" << campoMedio(25, ' ', to_string(tiempos_gausiana[i]), AZUL) << "\t" << campoMedio(25, ' ', to_string(resultados_lineal[i]), AZUL) << "\t" << campoMedio(25, ' ', to_string(resultados_gausiana[i]), AZUL) << endl;
    }
    return 0;
}