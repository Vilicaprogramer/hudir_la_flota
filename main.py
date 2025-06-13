import utils
import os

tablero_maquina = utils.crea_tablero()
tablero_maquina_visible = utils.crea_tablero()
tablero_usuario_barcos = utils.crea_tablero()
tablero_usuario_tiros = utils.crea_tablero()
for b in utils.barcos:
    tablero_maquina = utils.crea_barco_aleatorio(tablero_maquina, b)

print("La máquina ya está preparada es tu turno de colocar tus barcos")

utils.mostrar_tablero(tablero_usuario_barcos)

barcos_puestos =  utils.barcos.copy()
while len(barcos_puestos) != 0:
    for b in barcos_puestos:
        try:
            print(f"Es el turno del barco de {b} puntos de eslora")
            fila = int(input("Introduce el número de fila: "))
            columna = input("Introduce la letra de la columna: ").upper()
            direccion = input("Introduce N,S,O,E para ver la dirección del varco: ").upper()
            tablero_usuario_barcos = utils.crea_barco_usuario(tablero_usuario_barcos, b, fila, columna, direccion)
            utils.mostrar_tablero(tablero_usuario_barcos)
            barcos_puestos.remove(b)
        except:
            utils.mostrar_tablero(tablero_usuario_barcos)
            print("Ahí no se puede colocar vuelvelo a intentar")

os.