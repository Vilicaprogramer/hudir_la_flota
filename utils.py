'''Archivo donde vamos a crear las funciones que interactuarán con el usuario y con la máquina.
Habrá un apartado de funciones que interactuarán con el usuario y otro apartado con las funciones
que trabajarán con la máquina'''
import random
import numpy as np
import time 


# Funcionalidades del programa

# Variable con el titulo del juego descargado de https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
banner = r'''
  |   |  |   |   \  |  __ \ _ _|   _ \       |         \         ____|  |       _ \ __ __|   \    
  |   |  |   |    \ |  |   |  |   |   |      |        _ \        |      |      |   |   |    _ \   
  ___ |  |   |  |\  |  |   |  |   __ <       |       ___ \       __|    |      |   |   |   ___ \  
 _|  _| \___/  _| \_| ____/ ___| _| \_\     _____| _/    _\     _|     _____| \___/   _| _/    _\ 
                                                                                                  
'''

# Lista de números que representan el número de barcos y su eslora
#barcos = [5,4,4,3,3,3,2,2,1,1,1,1]
barcos = [10,1]

def lanza_moneda():
    '''Función que simula un lanzamiento de moneda para elegir quien comienza'''
    while True:
        moneda = input('Elige cara o cruz para ver quien empieza: ').lower()
        if moneda not in ['cara', 'cruz']:
            print('Eso no es una opción correcta, intentalo de nuevo')
        else:
            cara_aleatoria = random.choice(['cara', 'cruz'])
            for i in range(3,0,-1):
                print(i)
                time.sleep(1)

            if moneda != cara_aleatoria:
                return f'{cara_aleatoria.capitalize()} comienza la máquina'
            else:
                return f'{cara_aleatoria.capitalize()} comienza el jugador humano'


def verificar_tablero(tablero):
    '''Función que al ser llamada verifica el tablero dado iterando por cada fila verifiacndo si queda 
    algun barco sin disparar en el tablero'''
    if any("O" in fila for fila in tablero):
        return True
    else:
        return False

# Funciones de la máquina
def crea_tablero(lado = 10, simbolo = "~"):
    '''Función que por defecto crea un tablero de 10x10 relleno con el simbolo "~"'''
    tablero = np.full((lado,lado),simbolo)
    return tablero


def mostrar_tablero(tablero):
    '''Función que muestra por pantalla el tablero pasado como argumento, y lo muestra con el formato,
    filas numeradas del 1 al 10 y columnas con el encabezado marcado con letras de la A a la J'''
    print( '     A ',' B ',' C ',' D ',' E ',' F ',' G ',' H ',' I ',' J ')
    for i in range(len(tablero)):
        if i < 9:
            print(f'{i+1}- {tablero[i]}')
        else:
            print(f'{i+1}-{tablero[i]}')

def coloca_barco_plus(tablero, barco):
    '''Función que nos devuelve el tablero si puede colocar el barco, si no devuelve False, 
    y avisa por pantalla'''
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




def crea_barco_aleatorio(tablero, eslora):
    '''Función que genera barcos y los coloca en el tablero de forma aleatoria'''
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

def recibir_disparo_humano(tablero1, tablero2):
    '''Función que simula el turno de disparar del usuario'''
    while True:
        posicion = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9}
        num_max_filas = tablero1.shape[0]
        num_max_columnas = tablero1.shape[1]
        coordenada = (random.randint(0,num_max_filas - 1), random.randint(0,num_max_columnas - 1))
        letra = [clave for clave, valor in posicion.items() if valor == coordenada[1]]
        print(f'La máquina ha elegido la fila {coordenada[0] + 1} y la columna {letra[0]}')
        time.sleep(2)
        if tablero1[coordenada] == "O":
            tablero1[coordenada] = "X"
            tablero2[coordenada] = "X"
            print("Tocado")
            return False
        elif tablero2[coordenada] == "X" or tablero2[coordenada] == "~":
            print("Ahí ya has disparado, dispara a otro sitio!!")
        else:
            tablero2[coordenada] = "~"
            print("Agua")
            return False


# Funciones de usuario

def crea_barco_usuario(tablero, eslora):
    '''Función que para colocar los diferentes barcos en el tablero del usuario humano'''    
    while True:
        posicion = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9}
        barco = []
        try:
            fila = int(input("Introduce el número de fila: "))
            columna = input("Introduce la letra de la columna: ").upper()
            pieza_original = (fila - 1, posicion[columna])
            barco.append(pieza_original)
            fila = pieza_original[0]
            columna = pieza_original[1]
            if eslora != 1:
                orientacion = input("Introduce N,S,O,E para ver la dirección del barco: ").upper()
            # Construimos el hipotetico barco
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
            else:
                barco.append(pieza_original)
            tablero_temp = coloca_barco_plus(tablero, barco)
            if type(tablero_temp) == np.ndarray:
                return tablero_temp
        except:
            print('Has introducido un dato erroneo, vuelve a intentarlo')


def recibir_disparo_maquina(tablero1, tablero2):
    '''Función que simula el turno de disparar de la máquina'''
    while True:
        try:
            fila = int(input("Introduce el número de fila: "))
            columna = input("Introduce la letra de la columna: ").upper()
            posicion = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8,'J': 9}
            coordenada = (fila - 1, posicion[columna])
            print(f'Tu elección ha sido la fila {fila} y la columna {columna}')
            time.sleep(2)
            if tablero1[coordenada] == "O":
                tablero1[coordenada] = "X"
                tablero2[coordenada] = "X"
                print("Tocado")
                return False
            elif tablero2[coordenada] == "X" or tablero2[coordenada] == "~":
                print("Ahí ya has disparado, dispara a otro sitio!!")
            else:
                tablero2[coordenada] = "~"
                print("Agua")
                return False
        except:
            print('Has introducido un dato erroneo, vuelve a intentarlo')