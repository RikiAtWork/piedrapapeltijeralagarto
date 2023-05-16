import random
import sys

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
lagarto = 'lagarto'
opcion = [piedra, papel, tijera, lagarto]
partidas = [[papel, piedra], [tijera, papel], [piedra, tijera],
            [lagarto, papel], [piedra, lagarto], [tijera, lagarto]]
no_partidas = [[piedra, papel], [papel, tijera], [tijera, piedra],
               [papel, lagarto], [lagarto, piedra], [lagarto, tijera]]


def generar_movimientos():
    movimient = random.choice(opcion)
    return movimient


def verificar_movimientos(usario_mov, ordenador_mov):
    if [usario_mov, ordenador_mov] in partidas:
        return 1
    elif [usario_mov, ordenador_mov] in no_partidas:
        return -1
    return 0


print("JUEGO : Piedra, papel, tijera y lagarto")
nombre = input("Introduce tu nombre: ")

while True:
    opciones = input("Quieres jugar? (s/n): ")
    if 's' in opciones.lower():
        ordenador_movimiento = generar_movimientos()
        while True:
            movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel "
                               "/ 't' para tijeras / 'l' para lagarto): ").lower()
            usuario_movimiento = ""
            if movimiento.upper() == "TERMINAR":
                sys.exit("Tienes miedo?")

            if movimiento in ['p', 'a', 't', 'l']:
                if movimiento == 'p':
                    usuario_movimiento = piedra
                elif movimiento == 'a':
                    usuario_movimiento = papel
                elif movimiento == 't':
                    usuario_movimiento = tijera
                elif movimiento == 'l':
                    usuario_movimiento = lagarto

                print(f"Elección del ordenador: {ordenador_movimiento}")
                print(f"Elección del usuario: {usuario_movimiento}")

                if verificar_movimientos(usuario_movimiento, ordenador_movimiento) == 1:
                    print(f"Gana el usuario, {nombre} !!!")
                elif verificar_movimientos(usuario_movimiento, ordenador_movimiento) == -1:
                    print("Gana el ordenador !!!")
                elif verificar_movimientos(usuario_movimiento, ordenador_movimiento) == 0:
                    print("Empate !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in opciones.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
