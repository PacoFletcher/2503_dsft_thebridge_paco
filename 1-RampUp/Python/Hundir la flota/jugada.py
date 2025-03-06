import random
import tablero
import funciones

turno = 0
tirada = 0
vidas1 = 10
vidas2 = 10


M1 = tablero.M1
M2 = tablero.M2
C1 = tablero.C1
C2 = tablero.C2

while vidas1 > 0 and vidas2 > 0:
    print(f"Tirada número {tirada}, turno del jugador {turno%2 + 1}")
    if turno % 2 == 0:
        acierto = True
        while acierto:
            x = int(input("Introduce la primera coordenada de la tirada:"))
            y = int(input("Introduce la segunda coordenada de la tirada:"))
            if funciones.dentro(x,y) and C1[x][y] == 0:
                tirada += 1
                if M2[x][y] == 'O':
                    C1[x][y] = 'A'
                    print(f"Coordenada ({x},{y}): Agua. Turno del otro jugador")
                    turno += 1
                    acierto = False
                else:
                    C1[x][y] = 'T'
                    vidas2 -= 1
                    print(f"Coordenada ({x},{y}): Tocado. Vuelve a tirar")
            else:
                print(f"Coordenada ({x},{y}) fuera del tablero o ya visitada, prueba otra combinación") 
    else:
        acierto = True
        while acierto:
            # Al ser el turno de la máquina, la tirada será aleatoria
            x = random.randint(0,9)
            y = random.randint(0,9)
            if funciones.dentro(x,y) and C2[x][y] == 0:
                tirada += 1
                if M1[x][y] == 'O':
                    C2[x][y] = 'A'
                    print(f"Coordenada ({x},{y}): Agua. Turno del otro jugador")
                    turno += 1
                    acierto = False
                else:
                    C2[x][y] = 'T'
                    vidas2 -= 1
                    print(f"Coordenada ({x},{y}): Tocado. Vuelve a tirar")
            else:
                print("Fuera del tablero o ya visitada, prueba otra combinación")
if vidas1 == 0:
    print("Has perdido")
else:
    print("¡Enhorabuena! \n¡Has ganado!")