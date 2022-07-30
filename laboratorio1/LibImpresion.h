#include <vector>
#include <string>
// Colores de impresion
#define RESET "\033[0m"
#define ROJO "\033[31m"
#define VERDE "\033[32m"
#define AZUL "\033[34m"
#define AMARILLO "\033[33m"
#define MAGENTA "\033[35m"
#define AGUAMARINA "\033[36m"
#define NORMAL ""
using namespace std;

string campoMedio(int espacios, char caracter, string cadena, string COLOR)
{
    // Imprimir la cadela en la mitad de los espacios
    int tamanioCadena = cadena.size();
    int espaciosSinCadena = espacios - tamanioCadena;
    int espaciosDerecha = espaciosSinCadena / 2;
    int espaciosIzquierda = espaciosSinCadena - espaciosDerecha;
    string espaciosIzquierdaString = "";
    string espaciosDerechaString = "";
    // Imprimir espacios izquierda
    for (int i = 0; i < espaciosIzquierda; i++)
    {
        espaciosIzquierdaString += caracter;
    }
    // Imprimir espacios derecha
    for (int i = 0; i < espaciosDerecha; i++)
    {
        espaciosDerechaString += caracter;
    }
    // Retornar cadena
    return COLOR + espaciosIzquierdaString + cadena + espaciosDerechaString + RESET;
}

void tablaMedia(int columnas, int filas, vector<string> cabecera, vector<vector<string>> datos, string COLOR_CABECERA, string COLOR_DATOS)
{
    // calcular cual es el tamaño de la mayor cadena de la cabecera
    int espacios = 0;
    for (int i = 0; i < cabecera.size(); i++)
    {
        if (cabecera[i].size() > espacios)
        {
            espacios = cabecera[i].size();
        }
    }
    // Imprimir cabecera
    for (int i = 0; i < cabecera.size(); i++)
    {
        std::cout << campoMedio(espacios, ' ', cabecera[i], COLOR_CABECERA);
        if (i < cabecera.size() - 1)
        {
            std::cout << "|";
        }
    }
    std::cout << endl;
    // Imprimir datos
    for (int i = 0; i < filas; i++)
    {
        for (int j = 0; j < datos[i].size(); j++)
        {
            std::cout << campoMedio(espacios, ' ', datos[i][j], COLOR_DATOS);
            if (j < datos[i].size() - 1)
            {
                std::cout << "|";
            }
        }
        std::cout << endl;
    }
}

void tablaMediaDesdeHasta(int columnas, int filas, vector<string> cabecera, vector<vector<string>> datos, string COLOR_CABECERA, string COLOR_DATOS, int desde, int hasta)
{
    // calcular cual es el tamaño de la mayor cadena de la cabecera
    int espacios = 0;
    for (int i = 0; i < cabecera.size(); i++)
    {
        if (cabecera[i].size() > espacios)
        {
            espacios = cabecera[i].size();
        }
    }
    // Imprimir cabecera
    for (int i = 0; i < cabecera.size(); i++)
    {
        std::cout << campoMedio(espacios, ' ', cabecera[i], COLOR_CABECERA);
        if (i < cabecera.size() - 1)
        {
            std::cout << "|";
        }
    }
    std::cout << endl;
    // Imprimir datos
    for (int i = desde; i < hasta; i++)
    {
        for (int j = 0; j < datos[i].size(); j++)
        {
            std::cout << campoMedio(espacios, ' ', datos[i][j], COLOR_DATOS);
            if (j < datos[i].size() - 1)
            {
                std::cout << "|";
            }
        }
        std::cout << endl;
    }
}

void datoMedio(vector<string> cabecera, vector<string> dato, string COLOR_CABECERA, string COLOR_DATOS, bool imprimirCabecera)
{
    // calcular cual es el tamaño de la mayor cadena de la cabecera
    int espacios = 0;
    for (int i = 0; i < cabecera.size(); i++)
    {
        if (cabecera[i].size() > espacios)
        {
            espacios = cabecera[i].size();
        }
    }
    if (imprimirCabecera)
        // Imprimir cabecera
        for (int i = 0; i < cabecera.size(); i++)
        {
            std::cout << campoMedio(espacios, ' ', cabecera[i], COLOR_CABECERA);
            if (i < cabecera.size() - 1)
            {
                std::cout << "|";
            }
        }
    std::cout << endl;
    // Imprimir datos
    for (int i = 0; i < dato.size(); i++)
    {
        std::cout << campoMedio(espacios, ' ', dato[i], COLOR_DATOS);
        if (i < dato.size() - 1)
        {
            std::cout << "|";
        }
    }
    std::cout << endl;
}