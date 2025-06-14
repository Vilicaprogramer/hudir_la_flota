import utils
import os
import time

print(utils.banner)
print("Cargando....")
time.sleep(4)
os.system('cls')

print('BIENVENIDO COMENZAMOS EL JUEGO!!')
print()
print('Preparando al jugador Máquina...')
print()
time.sleep(4)
os.system('cls')

tablero_maquina = utils.crea_tablero()
tablero_maquina_visible = utils.crea_tablero(simbolo = " ")
tablero_usuario_barcos = utils.crea_tablero()
tablero_usuario_tiros = utils.crea_tablero(simbolo = " ")
for b in utils.barcos:
    tablero_maquina = utils.crea_barco_aleatorio(tablero_maquina, b)

print("La máquina ya está preparada es tu turno de colocar tus barcos")

utils.mostrar_tablero(tablero_usuario_barcos)
print("AHORA ES TU TRUNO")

print("Comienza a colocar tus barcos")
barcos_puestos =  utils.barcos.copy()
while len(barcos_puestos) != 0:
    for b in barcos_puestos:
        try:
            print(f"Es el turno del barco de tamaño {b}")
            tablero_usuario_barcos = utils.crea_barco_usuario(tablero_usuario_barcos, b)
            os.system('cls')
            utils.mostrar_tablero(tablero_usuario_barcos)
            barcos_puestos.remove(b)
        except:
            utils.mostrar_tablero(tablero_usuario_barcos)
            print("Ahí no se puede colocar vuelvelo a intentar")

print('COMIENZA EL JUEGO!!')
print()
primer_jugador = utils.lanza_moneda()
print(primer_jugador)
time.sleep(2)
os.system('cls')

turno = primer_jugador.split()[-1]
while utils.verificar_tablero(tablero_maquina) and utils.verificar_tablero(tablero_usuario_barcos):
    if turno == 'máquina':
            print()
            print('Turno de la máquina')
            print()
            utils.mostrar_tablero(tablero_maquina_visible)
            print()
            utils.recibir_disparo_humano(tablero_usuario_barcos,tablero_maquina_visible)
            time.sleep(4)
            os.system('cls')
            print()
            print('Turno de la máquina')
            print()
            utils.mostrar_tablero(tablero_maquina_visible)
            print()
            time.sleep(3)
            os.system('cls')
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
        os.system('cls')
        print()
        print('Turno del Jugador humano')
        print()
        utils.mostrar_tablero(tablero_usuario_tiros)
        utils.mostrar_tablero(tablero_usuario_barcos)
        print()
        time.sleep(3)
        os.system('cls')
        turno = 'máquina'

if turno == 'máquina':
     print('WINNER!!!')
     print('ENHORABUENA JUGADOR')
     print('Espero que hayas disfrutado del juego')
else:
    print('YOU LOSE')
    print('Más suerte la proxima vez')
    print('Espero que hayas disfrutado del juego')
     