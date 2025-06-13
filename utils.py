'''Archivo donde vamos a crear las funciones que interactuarán con el usuario y con la máquina.
Habrá un apartado de funciones que interactuarán con el usuario y otro apartado con las funciones
que trabajarán con la máquina'''
import random
import numpy as np

barcos = [5,4,4,3,3,3,2,2,1,1,1,1]

# Funciones de la máquina
def crea_tablero(lado = 10):
    tablero = np.full((lado,lado),"~")
    return tablero


def mostrar_tablero(tablero):
    print( '     A ',' B ',' C ',' D ',' E ',' F ',' G ',' H ',' I ',' J ')
    for i in range(len(tablero)):
        if i < 9:
            print(f'{i+1}- {tablero[i]}')
        else:
            print(f'{i+1}-{tablero[i]}')

def coloca_barco_plus(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            return False
        if columna <0 or columna>= num_max_columnas:
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp




def crea_barco_aleatorio(tablero, eslora, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp

        

        



# Funciones de usuario

def crea_barco_usuario(tablero, eslora, fila, columna ,punto_cardinal):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        posicion = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9}
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (fila - 1, posicion[columna])
        barco.append(pieza_original)
        orientacion = punto_cardinal
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp