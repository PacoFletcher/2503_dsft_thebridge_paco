import random
import tablero
import funciones

turno = 0
tirada = 1
vidas1 = 20
vidas2 = 20

M1 = tablero.M1
M2 = tablero.M2
C1 = tablero.C1
C2 = tablero.C2
flota1 = tablero.flota1
flota2 = tablero.flota2


## ACTUALMENTE ESTOY PULIENDO LAS TIRADAS DE LOS JUGADORES
# PROBLEMAS CON LA FUNCIÓN PINTA
# PROBLEMAS CON EL CONTEO DE TIRADAS
# PARECE QUE EL DUMMY FUNCIONA BIEN


while vidas1 > 0 and vidas2 > 0:
    print(f"Tirada número {tirada}, turno del jugador {turno%2 + 1}")
    # ESTA FUNCIÓN SE IMPLEMENTARÁ EN LA VERSIÓN DEFINITIVA Y COMPRENDERÁ 
    # EL CÓDIGO QUE ESTÁ DENTRO DEL BUCLE
    ###############################
    # jugada(turno)
    ###############################

    if turno % 2 == 0:
        # funciones.turno1()
        acierto = True
        while acierto and vidas2 > 0:
            # Antes de cada tirada, imprimimos por pantalla la matriz 
            # que almacena los resultados de las tiradas para facilitar la jugabilidad
            funciones.imprime_tablero(C1)
            """for i in range(len(C1)):
                for j in range(len(C1[i])):
                    print(C1[i][j], end = " ")
                print("")"""
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
                    t = (x,y)
                    aux = 0
                    for i in range(len(flota2)):
                        if t in flota2[i].coord.keys():
                            flota2[i].coord[t] = True
                            flota2[i].vida -= 1
                            aux = i
                    if flota2[aux].vida == 0:
                        print(f"Coordenada ({x},{y}): Tocado y hundido. Vuelve a tirar")
                        C = C1
                        C1 = funciones.pinta(C,flota2[aux])
                    else:
                        print(f"Coordenada ({x},{y}): Tocado. Vuelve a tirar")
                    vidas2 -= 1
            else:
                print(f"Coordenada ({x},{y}) fuera del tablero o ya visitada, prueba otra combinación") 
    else:
        """
        match dif:
            # Todas las tiradas de la máquina serán aleatorias.
            case 0:
                funciones.turno20()
            
            # La máquina recordará las últimas tiradas y, si recientemente ha tocado pero no hundido un barco, 
            # se moverá en el entorno de esa celda. 
            case 1:
                funciones.turno21()

            # Versión mejorada de la dificultad 1, donde además realizará más de una comprobación
            # para elegir una tirada favorable.
            case 2:
                funciones.turno22()

            # Nivel (casi) imposible, en el que la máquina tiene acceso a nuestro vector flota, por lo que en un solo turno ganará la partida
            case 3:
                funciones.turno23() 
        """
        acierto = True
        while acierto and vidas1 > 0:
            for i in range(len(C2)):
                for j in range(len(C2[i])):
                    print(C2[i][j], end = " ")
                print("")
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
                    vidas1 -= 1
                    t = (x,y)
                    aux = 0
                    for i in range(len(flota1)):
                        if t in flota1[i].coord.keys():
                            flota1[i].coord[t] = True
                            flota1[i].vida -= 1
                            aux = i
                    if flota1[aux].vida == 0:
                        print(f"Coordenada ({x},{y}): Tocado y hundido. Vuelve a tirar")
                        C = C2
                        C2 = funciones.pinta(C,flota2[aux])
                    else:
                        print(f"Coordenada ({x},{y}): Tocado. Vuelve a tirar")
            else:
                print("Fuera del tablero o ya visitada, prueba otra combinación")
if vidas1 == 0:
    print("Has perdido")
else:
    print("¡Enhorabuena! \n¡Has ganado!")