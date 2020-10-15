#Esta una recreación del juego piedra, papel o tijeras en Python

import random
import sys
aleatorio = random.randrange(1,4)
eleccion_m = ''

while True:
    print("Elige Piedra(p), Papel(a) o Tijera(t) [Presiona s para salir]")
    eleccion = input().lower()

    if eleccion == 'p' or eleccion == 'a' or eleccion == 't':
        break
    if eleccion == 's':
        print("Gracias por jugar")
        sys.exit()

if aleatorio == 1:
    eleccion_m = 'p'
    print("La computadora selecciono Piedra")
elif aleatorio == 2:
    eleccion_m = 'a'
    print("La computadora selecciono Papel")
else:
    eleccion_m = 't'
    print("La computadora selecciono Tijeras")

if eleccion == 'p':
    print("Seleccionaste Piedra")
elif eleccion == 'a':
    print("Seleccionaste Papel")
else:
    print("Seleccionaste Tijeras")

if eleccion == eleccion_m:
    print("Empate")
elif eleccion == 'a' and eleccion_m == 't':
    print("Perdiste")
elif eleccion == 't' and eleccion_m == 'p':
    print("Perdiste")
elif eleccion_m == 'a' and eleccion == 'p':
    print("Perdiste")
elif eleccion_m == 'a' and eleccion == 't':
    print("Ganaste")
elif eleccion_m == 't' and eleccion == 'p':
    print("Ganaste")
elif eleccion == 'a' and eleccion_m == 'p':
    print("Ganaste")