import funciones
import random
#import numpy as np

class barco:

    def __init__(self):
        self.coord = {}
        self.vidas = 0
        pass

def dentro(x,y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    return False

def mira(M,x,y):
    for i in range(-1,2):
            for j in range(-1,2):
                if dentro(x-j,y-i):
                    if M[x-j][y-i] != 0:
                        return False
    return True
def valido(M,l,v,j,x,y):
    # Analizaremos celda a celda.
    # Si el barco está en posición vertical, modificaremos la coordenada x 
    if v == True:
        for i in range(0,l):
            if not mira(M,x+i + 10*j,y):
                return False
    # Si el barco está en posición horizontal, modificaremos la coordenada y    
    else:
        for i in range(0,l):
            if not mira(M,x + 10*j,y+i):
                return False
        
    return True


def set_mapa2(M, l, B, j):
    # el parámetro v nos indica si el barco que estamos colocando estará en posición vertical u horizontal
    v = random.randint(0,1)
    
    # Empezaremos a construir el barco eligiendo la primera casilla que este ocupará.
    # Si es vertical, la coordenada y (eje vertical) como máximo podrá ser 9 - l + 1, para evitar salirnos del mapa 
    if v == 1:
        while True:
            x = random.randint(0,9-l+1)
            y = random.randint(0,9)
            # En esta función comprobaremos si para la posición inicial establecida, 
            # no hay ninguna casilla conflictiva antes de proceder a asignar estas 
            # posiciones a nuestro barco definitivamente.
            # Si valido detectara alguna casilla conflictiva, se volverían a generar 
            # dos coordenadas aleatorias hasta dar con una combinación factible.
            if valido(M,l,v,j,x,y):
                break
        # Una vez validadas las cordenadas (x,y), procedemos a:
        # 1. Ubicar el barco en nuestro mapa
        # 2. Añadir los atributos de la clase barco a nuestra lista
        for i in range(0,l):
            M[x+i + j*10][y] = 'B'
            t = (x+i,y)
            B[-1].coord[t] = False
        B[-1].vida = len(B[-1].coord.keys())
            #b.coord[str(x, int(y+i))] = False
    # Lo mismo ocurre si el barco está en posición horizontal, 
    # respectivamente con la variable x (eje horizontal)
    else:
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9-l+1)
            if valido(M,l,v,j,x,y):
                break
        for i in range(0,l):
            M[x + j*10][y+i] = 'B'
            t = (x,y+i)
            B[-1].coord[t] = False
        B[-1].vida = len(B[-1].coord.keys())


A = [[0 for i in range(20)] for i in range (20)]
B = []
for i in (0,2):
    for l in (4,0,-1):
        for i in (0,5-l):
            b = barco()
            B.append(b)
            v = random.randint(0,1)
            set_mapa2(A,l,B,i)



funciones.imprime_tablero()

for i in range(0,10):
    for j in range(0,10):
        print(A[i][j], end = " ")
    print("")

print("-"*100)

for i in range(10,20):
    for j in range(0,10):
        print(A[i][j], end = " ")
    print("")