import funciones
import random


class barco:

    def __init__(self):
        self.coord = {}
        self.vidas = 0
        pass


def imprime_tablero2(A,j,c):
    for i in range(-1,10):
        if i == -1:
            print (" ", end = " | ")
        else:
            print(i, end = " | ")
    print("")
    print("-"*43)
    for x in range(10):
        for y in range(11):
            if y == 0:
                print(x, end  = " | ")
            else:
                print(A[x+10*j][y-1+10*c], end = " | ")
        print("")
        print("-"*43)


def dentro(x,y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    return False

def mira2(A,j,x1,y1):
    for a in range(-1,2):
        for b in range(-1,2):
            if dentro(x1-a,y1-b):
                print(x1-a,y1-b)
                if A[x1-a + 10*j][y1-b] != 0:
                    return False
    return True
def valido2(A,l,v,j,x1,y1):
    # Analizaremos celda a celda.
    # Si el barco está en posición vertical, modificaremos la coordenada x 
    if v == True:
        for i in range(0,l):
            if not mira2(A,j,x1+i,y1):
                return False
    # Si el barco está en posición horizontal, modificaremos la coordenada y    
    else:
        for i in range(0,l):
            if not mira2(A,j,x1 ,y1+i):
                return False
        
    return True


def set_mapa2(A, l, B, j):
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
            if valido2(A,l,v,j,x,y):
                break
        # Una vez validadas las cordenadas (x,y), procedemos a:
        # 1. Ubicar el barco en nuestro mapa
        # 2. Añadir los atributos de la clase barco a nuestra lista
        for i in range(0,l):
            A[x+i + j*10][y] = 'B'
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
            if valido2(A,l,v,j,x,y):
                break
        for i in range(0,l):
            A[x + j*10][y+i] = 'B'
            t = (x,y+i)
            B[-1].coord[t] = False
        B[-1].vida = len(B[-1].coord.keys())


A = [[0 for i in range(20)] for i in range (20)]
B = []
for j in range(0,2):
    for l in range(4,0,-1):
        for i in range(0,5-l):
            b = barco()
            B.append(b)
            set_mapa2(A,l,B,j)
    imprime_tablero2(A,j,0)





