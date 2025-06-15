import utils
import os
import time

'''main.py es el archivo principal, donde se llama a las funciones del juego y se aplica la lógica del juego,
Tras mostrar el título y cargar el tablero de la máquina de forma aleatoria, solicitará la colocación de los 
diferentes barcos del tablero al usuario.'''

print(utils.banner)
print("Cargando....")
time.sleep(4)
os.system('cls')

print('BIENVENIDO COMENZAMOS EL JUEGO!!')
print()
print('Preparando al jugador Máquina...')
print()
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')

# Creación de los 4 talberos gracias a la función crea tableros del archivo utils.py
tablero_maquina = utils.crea_tablero()
tablero_maquina_visible = utils.crea_tablero(simbolo = " ")
tablero_usuario_barcos = utils.crea_tablero()
tablero_usuario_tiros = utils.crea_tablero(simbolo = " ")
for b in utils.barcos:
    tablero_maquina = utils.crea_barco_aleatorio(tablero_maquina, b)

print("La máquina ya está preparada es tu turno de colocar tus barcos")

utils.mostrar_tablero(tablero_usuario_barcos)
print("AHORA ES TU TRUNO")

# Llamamos a la lista de barcos que está en utils.py y nos aseguramos que se colocan todos gracias al bucle while
print("Comienza a colocar tus barcos")
barcos_puestos =  utils.barcos.copy()
while len(barcos_puestos) != 0:
    for b in barcos_puestos:
        try:
            print(f"Es el turno del barco de tamaño {b}")
            tablero_usuario_barcos = utils.crea_barco_usuario(tablero_usuario_barcos, b)
            os.system('cls' if os.name == 'nt' else 'clear')
            utils.mostrar_tablero(tablero_usuario_barcos)
            barcos_puestos.remove(b)
        except:
            utils.mostrar_tablero(tablero_usuario_barcos)
            print("Ahí no se puede colocar vuelvelo a intentar")

print('COMIENZA EL JUEGO!!')
print()
# Para que no siempre empiece o el jugador máquina o el jugador humano, creamos una función lanza moneda.
primer_jugador = utils.lanza_moneda()
print(primer_jugador)
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

# Variable que iremos cambiando entre 'humano' y 'máuina' mientras que detecte que en los dos tableros queda 
# alguna 'O'
turno = primer_jugador.split()[-1]
# Lógica del juego que llama a las diferentes funciones de disparo según el jugador que le toque
while utils.verificar_tablero(tablero_maquina) and utils.verificar_tablero(tablero_usuario_barcos):
    if turno == 'máquina':
            print()
            print('Turno de la máquina')
            print()
            utils.mostrar_tablero(tablero_maquina_visible)
            print()
            utils.recibir_disparo_humano(tablero_usuario_barcos,tablero_maquina_visible)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            print('Turno de la máquina')
            print()
            utils.mostrar_tablero(tablero_maquina_visible)
            print()
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            turno = 'humano'
    else:
        print()
        print('Turno del Jugador humano')
        print()
        utils.mostrar_tablero(tablero_usuario_tiros)
        utils.mostrar_tablero(tablero_usuario_barcos)
        print()
        utils.recibir_disparo_maquina(tablero_maquina, tablero_usuario_tiros)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print('Turno del Jugador humano')
        print()
        utils.mostrar_tablero(tablero_usuario_tiros)
        utils.mostrar_tablero(tablero_usuario_barcos)
        print()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        turno = 'máquina'

# Una vez detectado que uno de los dos tableros ya no tinen ninguna 'O' el juego se interrumpe y 
# mostramos el mensaje de ganador o perdedor.
if turno == 'máquina':
     print('WINNER!!!')
     print('ENHORABUENA JUGADOR')
     print('Espero que hayas disfrutado del juego')
else:
    print('YOU LOSE')
    print('Más suerte la proxima vez')
    print('Espero que hayas disfrutado del juego')
     