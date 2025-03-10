import funciones
import random

def set_mapa2(M, l, flota, j):
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
            if valido(M,x,y,l,v):
                break
        # Una vez validadas las cordenadas (x,y), procedemos a:
        # 1. Ubicar el barco en nuestro mapa
        # 2. Añadir los atributos de la clase barco a nuestra lista
        for i in range(0,l):
            M[x+i + j*10][y] = 'B'
            t = (x+i,y)
            flota[-1].coord[t] = False
        flota[-1].vida = len(flota[-1].coord.keys())
            #b.coord[str(x, int(y+i))] = False
    # Lo mismo ocurre si el barco está en posición horizontal, 
    # respectivamente con la variable x (eje horizontal)
    else:
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9-l+1)
            if valido(M, x,y,l,v):
                break
        for i in range(0,l):
            M[x + j*10][y+i] = 'B'
            t = (x,y+i)
            flota[-1].coord[t] = False
        flota[-1].vida = len(flota[-1].coord.keys())


A = [[0 for i in range(20)] for i in range (20)]
B = []
for i in (0,2):
    for l in (4,0,-1):
        for i in (0,5-l):
            v = random.randint(0,1)
            set_mapa2(A,l,flota,i)

