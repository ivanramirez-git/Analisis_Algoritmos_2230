#include <iostream>
#include <vector>

using namespace std;

// Comprobar si la suma de dos numeros de una lista tiene un restultado dado
vector<pair<int,int> >comprobar_suma_dos(vector<int> lista, int valor)
{
    vector<pair<int,int> > resultados;
    for (int i = 0; i < lista.size(); i++)
    {
        for (int j = i + 1; j < lista.size(); j++)
        {
            if (lista[i] + lista[j] == valor)
            {
                resultados.push_back(make_pair(i,j));
            }
        }
    }
    return resultados;
}

// Comprobar si la suma de tres numeros de una lista tiene un restultado dado
vector<vector<int>> comprobar_suma_tres(vector<int> lista, int valor)
{
    vector<vector<int>> resultados;
    for (int i = 0; i < lista.size(); i++)
    {
        for (int j = i + 1; j < lista.size(); j++)
        {
            for (int k = j + 1; k < lista.size(); k++)
            {
                if (lista[i] + lista[j] + lista[k] == valor)
                {
                    vector<int> resultado;
                    resultado.push_back(i);
                    resultado.push_back(j);
                    resultado.push_back(k);
                    resultados.push_back(resultado);
                }
            }
        }
    }
    return resultados;
}
// pruebas
void prueba1()
{
    vector<int> lista;
    // 12, 23, 41, 36, 28, 54, 35, 46, 52, 19, 27
    lista.push_back(12);
    lista.push_back(23);
    lista.push_back(41);
    lista.push_back(36);
    lista.push_back(28);
    lista.push_back(54);
    lista.push_back(35);
    lista.push_back(46);
    lista.push_back(52);
    lista.push_back(19);
    lista.push_back(27);
    int numero = 74;

    vector<pair<int,int> > resultados = comprobar_suma_dos(lista, numero);
    if(resultados.size() == 0)
    {
        cout << "No hay resultados combinando dos numeros" << endl;
    }
    else
    {
        for (int i = 0; i < resultados.size(); i++)
        {
            cout << "(" << lista[resultados[i].first] << "," << lista[resultados[i].second] << ")" << endl;
        }
    }

    vector<vector<int>> resultados_tres = comprobar_suma_tres(lista, numero);
    if(resultados_tres.size() == 0)
    {
        cout << "No hay resultados combinando tres numeros" << endl;
    }
    else
    {
        for (int i = 0; i < resultados_tres.size(); i++)
        {
            cout << "(" << lista[resultados_tres[i][0]] << "," << lista[resultados_tres[i][1]] << "," << resultados_tres[i][2] << ")" << endl;
        }
    }

}

// main
int main()
{
    prueba1();
    return 0;
}