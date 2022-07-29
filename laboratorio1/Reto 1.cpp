// Una empresa de autopistas tiene instalada una camara que cuenta el numero de vehiculos que pasa por una autopista.
// Calcular cuantos coches y motos pasan por la autopista, con el numero de ruedas y el numero de vehiculos que pasan por la autopista.
#include <iostream>
#include <vector>

using namespace std;

// algoritmo donde se usen 2 for
pair<int, int> algoritmo_2for(int n_ruedas, int n_vehiculos)
{
    // retorna un par con el numero de coches y motos
    for (int coches = 0; coches <= n_vehiculos; coches++)
    {
        for (int motos = 0; motos <= n_vehiculos; motos++)
        {
            if (motos + coches == n_vehiculos)
            {
                if (n_ruedas == (coches * 4) + (motos * 2))
                {
                    return make_pair(coches, motos);
                }
            }
        }
    }
    return make_pair(0, 0);
}

// algoritmo donde se use 1 for
pair<int, int> algoritmo_1for(int n_ruedas, int n_vehiculos)
{
    for (int coches = 0; coches <= n_vehiculos; coches++)
    {
        int motos = n_vehiculos - coches;
        if (motos < 0 || coches < 0)
        {
            continue;
        }
        if (n_ruedas == (coches * 4) + (motos * 2))
        {
            return make_pair(coches, motos);
        }
    }
    return make_pair(0, 0);
}

// algoritmo sin usar for
pair<int, int> algoritmo_sinfor(int n_ruedas, int n_vehiculos)
{
    // retorna el numero de coches y motos
    // coches + motos = n_vehiculos
    // 4 * coches + 2 * motos = n_ruedas
    // coches = n_vehiculos - motos
    // 4 * (n_vehiculos - motos) + 2 * motos = n_ruedas
    // 4*n_vehiculos - 4*motos + 2*motos = n_ruedas
    // 4*n_vehiculos - 2*motos = n_ruedas
    // -2*motos = n_ruedas - 4*n_vehiculos
    // motos = (n_ruedas - 4*n_vehiculos) / -2
    // coches = n_vehiculos - motos
    int motos = (n_ruedas - 4 * n_vehiculos) / -2;
    int coches = n_vehiculos - motos;

    if (motos < 0 || coches < 0)
    {
        return make_pair(0, 0);
    }

    return make_pair(coches, motos);
}

// pruebas
void prueba1()
{
    cout << "Ingrese la cantidad de vehiculos: ";
    int n_vehiculos;
    cin >> n_vehiculos;
    cout << "Ingrese la cantidad de ruedas: ";
    int n_ruedas;
    cin >> n_ruedas;
    cout << "Calculando con 2 for..." << endl;
    pair<int, int> resultado = algoritmo_2for(n_ruedas, n_vehiculos);
    cout << "Coches: " << resultado.first << endl;
    cout << "Motos: " << resultado.second << endl;
    cout << "Calculando con 1 for..." << endl;
    resultado = algoritmo_1for(n_ruedas, n_vehiculos);
    cout << "Coches: " << resultado.first << endl;
    cout << "Motos: " << resultado.second << endl;
    cout << "Calculando sin for..." << endl;
    resultado = algoritmo_sinfor(n_ruedas, n_vehiculos);
    cout << "Coches: " << resultado.first << endl;
    cout << "Motos: " << resultado.second << endl;
}

// main
int main()
{
    prueba1();
    return 0;
}