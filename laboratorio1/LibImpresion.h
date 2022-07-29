
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