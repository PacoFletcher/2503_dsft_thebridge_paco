import random
import os
import tablero
import funciones
import variables

## ACTUALMENTE ESTOY PULIENDO LAS TIRADAS DE LOS JUGADORES
# PROBLEMAS CON LA FUNCIÓN PINTA
# PROBLEMAS CON EL CONTEO DE TIRADAS
# PARECE QUE EL DUMMY FUNCIONA BIEN

def partida(dif):
    os.system('varialbes.py')
    turno = 0
    tirada = 0
    vidas = [20,20]
    M = variables.P
    C = variables.Q
    F = variables.R

    futuro = []
    sec = False
    while vidas[0] > 0 and vidas[1] > 0:
        print(f"Tirada número {tirada}, turno del jugador {turno%2 + 1}")
        # ESTA FUNCIÓN SE IMPLEMENTARÁ EN LA VERSIÓN DEFINITIVA Y COMPRENDERÁ 
        # EL CÓDIGO QUE ESTÁ DENTRO DEL BUCLE
        ###############################
        # jugada(turno)
        ###############################
        turno = turno%2
        if turno == 0:
            # funciones.turno1()
            acierto = True
            while acierto and vidas[1] > 0:
                # Antes de cada tirada, imprimimos por pantalla la matriz 
                # que almacena los resultados de las tiradas para facilitar la jugabilidad
                funciones.imprime_tablero(C[turno])
                
                """for i in range(len(C1)):
                    for j in range(len(C1[i])):
                        print(C1[i][j], end = " ")
                    print("")"""
                turno, acierto =  funciones.tira1(M,C,F,vidas, turno)
                tirada += 1
                """
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
                        vidas[1] -= 1
                else:
                    print(f"Coordenada ({x},{y}) fuera del tablero o ya visitada, prueba otra combinación")
        """ 
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
            
            while acierto and vidas[0] > 0:
                funciones.imprime_tablero(C[turno])
                """for i in range(len(C2)):
                    for j in range(len(C2[i])):
                        print(C2[i][j], end = " ")
                    print("")"""
                # Al ser el turno de la máquina, la tirada será aleatoria

                
                if dif == 0:
                    turno, acierto =  funciones.dif_0(M,C,F,vidas, turno)
                        
                elif dif == 1:
                    #print("Work in Progress")
                    turno, acierto, sec = funciones.dif_1(M,C,F,vidas, turno, sec, futuro)
                    #turno, acierto =  funciones.dif0(M,C,F,vidas, turno)

                elif dif == 2:
                    turno, acierto, sec =  funciones.dif_2(M,C,F,vidas, turno, sec, futuro)
                
                else :
                    turno,acierto = funciones.dif_3(M,C,F,vidas,turno)
                
                tirada += 1

                """
                match dif:
                    case 0:
                    
                    case 1:
                    
                    case 2:
                    
                    case _:
                        tiradas = F[0].coord.keys()
                        while acierto and vidas[0] > 0
                            turno,acierto = funciones.dif3(M,C,F,vidas,turno,tiradas)

                """


                """
                x = random.randint(0,9)
                y = random.randint(0,9)
                if funciones.dentro(x,y) and C[turno][x][y] == 0:
                    tirada += 1
                    if M[(turno+1)%2][x][y] == 'O':
                        C[turno][x][y] = 'A'
                        print(f"Coordenada ({x},{y}): Agua. Turno del otro jugador")
                        turno += 1
                        acierto = False
                    else:
                        C[turno][x][y] = 'T'
                        vidas[0] -= 1
                        k = (x,y)
                        aux = 0
                        for i in range(len(F[turno])):
                            if k in F[(turno+1)%2][i].coord.keys():
                                F[(turno+1)%2][i].coord[k] = True
                                F[(turno+1)%2][i].vida -= 1
                                aux = i
                        if F[(turno+1)%2][aux].vida == 0:
                            print(f"Coordenada ({x},{y}): Tocado y hundido. Vuelve a tirar")
                            C[turno] = funciones.pinta(C,turno, F[turno][aux])
                        else:
                            print(f"Coordenada ({x},{y}): Tocado. Vuelve a tirar")
                else:
                    print("Fuera del tablero o ya visitada, prueba otra combinación")"""
            

    if vidas[0] == 0:
        print("Has perdido")
    else:
        print("¡Enhorabuena! \n¡Has ganado!")