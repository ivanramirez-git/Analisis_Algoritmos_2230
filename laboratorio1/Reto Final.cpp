/*
El censo debe tener 5 millones de registros
Los números deben estar de manera creciente partiendo del 1 o del 2, e ir aumentando o en 1 o en 2 unidades.
El nombre debe ser un string conformado de manera aleatoria de la siguiente cadena de texto: ["ABCDEFGIJAEIOULMNOPRSTUAEIOU"]
La edad es un numero random dentro de un rango de 18 a 99.
Los impuestos corresponden a un booleano tomado de manera aleatoria de un conjunto de 3 Trues y 1 False.
*/
#include <iostream>
#include "LibImpresion.h"
#include <string>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

// Funciones auxiliares
string generarNombre();
int generarEdad();
int generarImpuestos();

// Funciones principales
void Iniciar(int cantidad);
int buscarNombre(vector<vector<string>> datos, string nombre);                                  // Búsqueda Lineal
vector<int> buscarVariosNombres(vector<vector<string>> datos, string nombre);                   // Búsqueda Lineal con varios nombres
int buscarIndicador(vector<vector<string>> datos, string indicador);                            // Búsqueda Binaria
void imprimirRango(vector<string> cabecera, vector<vector<string>> datos, int inicio, int fin); // Imprimir rango de registros
int menu();

int main()
{
    srand(time(NULL));
    Iniciar(5000000);
    return 0;
}

string generarNombre()
{
    string nombre = "";
    string letras = "ABCDEFGIJAEIOULMNOPRSTUAEIOU";
    int tamanio = letras.size();
    for (int i = 0; i < 10; i++)
    {
        int posicion = rand() % tamanio;
        nombre += letras[posicion];
    }
    return nombre;
}

int generarEdad()
{
    return rand() % 82 + 18;
}

int generarImpuestos()
{
    return rand() % 4;
}

int generarIndicativo(int ant)
{
    return ant + rand() % 2 + 1;
}

void Iniciar(int cantidad)
{
    // Inicializar random
    srand(time(NULL));
    // Imprimir cabecera
    vector<string> cabecera;
    cabecera.push_back("Indicativo");
    cabecera.push_back("Nombre");
    cabecera.push_back("Edad");
    cabecera.push_back("Impuestos");
    // Imprimir datos
    vector<vector<string>> datos;
    for (int i = 0; i < cantidad; i++)
    {
        vector<string> dato;
        dato.push_back(to_string(generarIndicativo(i != 0 ? stoi(datos[i - 1][0]) : 0)));
        dato.push_back(generarNombre());
        dato.push_back(to_string(generarEdad()));
        dato.push_back(generarImpuestos() != 0 ? "True" : "False");
        datos.push_back(dato);
        if (i % 100000 == 0)
        {
            cout << "Creando censos: " << i << endl;
        }
    }
    // tablaMedia(4, cantidad, cabecera, datos, AZUL, VERDE);
    int opcion;
    do
    {
        /*
         cout << "1. Buscar por nombre" << endl;
        cout << "2. Buscar por indicador" << endl;

        cout << "4. Imprimir rango de datos" << endl;
        cout << "0. Salir" << endl;*/
        opcion = menu();
        switch (opcion)
        {
        case 1:
        {
            string nombre;
            cout << "Ingrese nombre: ";
            cin >> nombre;
            int posicion = buscarNombre(datos, nombre);
            if (posicion == -1)
            {
                cout << "No se encontro el nombre" << endl;
            }
            else
            {
                cout << "Posicion: " << posicion << endl;
                datoMedio(cabecera, datos[posicion], AZUL, VERDE);
            }
            break;
        }
        case 2:
        {
            string indicador;
            cout << "Ingrese indicador: ";
            cin >> indicador;
            int posicion = buscarIndicador(datos, indicador);
            if (posicion == -1)
            {
                cout << "No se encontro el indicador" << endl;
            }
            else
            {
                cout << "Posicion: " << posicion << endl;
                datoMedio(cabecera, datos[posicion], AZUL, VERDE);
            }
            break;
        }
        case 3:
        {
            string nombre;
            cout << "Ingrese nombre: ";
            cin >> nombre;
            vector<int> posiciones = buscarVariosNombres(datos, nombre);
            if (posiciones.size() == 0)
            {
                cout << "No se encontro el nombre" << endl;
            }
            else
            {
                cout << "Posiciones: ";
                for (int i = 0; i < posiciones.size(); i++)
                {
                    cout << posiciones[i] << " ";
                }
                cout << endl;
                for (int i = 0; i < posiciones.size(); i++)
                {
                    datoMedio(cabecera, datos[posiciones[i]], AZUL, VERDE);
                }
            }
            break;
        }
        case 4:
        {
            int inicio, fin;
            cout << "Ingrese idice inicial: ";
            cin >> inicio;
            cout << "Ingrese idice final: ";
            cin >> fin;
            imprimirRango(cabecera, datos, inicio, fin);
            break;
        }
        case 0:
            break;
        default:
            cout << "Opcion invalida" << endl;
            break;
        }
    } while (opcion != 0);
}

int buscarNombre(vector<vector<string>> datos, string nombre)
{
    int posicion = -1;
    for (int i = 0; i < datos.size(); i++)
    {
        if (datos[i][1] == nombre)
        {
            posicion = i;
            break;
        }
    }
    return posicion;
}

vector<int> buscarVariosNombres(vector<vector<string>> datos, string nombre)
{
    vector<int> posiciones;
    for (int i = 0; i < datos.size(); i++)
    {
        if (datos[i][1] == nombre)
        {
            posiciones.push_back(i);
        }
    }
    return posiciones;
}

int buscarIndicador(vector<vector<string>> datos, string indicador)
{
    int posicion = -1;
    for (int i = 0; i < datos.size(); i++)
    {
        if (datos[i][0] == indicador)
        {
            posicion = i;
            break;
        }
    }
    return posicion;
}

void imprimirRango(vector<string> cabecera, vector<vector<string>> datos, int inicio, int fin)
{
    for (int i = inicio; i <= fin; i++)
    {
        // void tablaMediaDesdeHasta(int columnas, int filas, std::vector<std::string> cabecera, std::vector<std::vector<std::string>> datos, std::string COLOR_CABECERA, std::string COLOR_DATOS, int desde, int hasta)
        tablaMediaDesdeHasta(4, fin - inicio + 1, cabecera, datos, AZUL, VERDE, i, i);
    }
}

int menu()
{
    int opcion;
    cout << "1. Buscar por nombre" << endl;
    cout << "2. Buscar por indicador" << endl;
    cout << "3. Buscar varios nombres iguales" << endl;
    cout << "4. Imprimir rango de datos" << endl;
    cout << "0. Salir" << endl;
    cout << "Ingrese opcion: ";
    cin >> opcion;
    return opcion;
}
