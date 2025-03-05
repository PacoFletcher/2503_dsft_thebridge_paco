"""
LIBRERÍAS
"""

import random


"""
CLASES
"""
class barco:
    coord = {}
    vida = 0
# Creamos dos matrices, M1 y M2, que corresponderán a los mapas de cada jugador
M1 = M2 = [['O' for i in range(10)] for i in range(10)]


# Creamos otras dos matrices, C1 y C2, que servirán a cada jugador para comprobar 
# las casillas ya visitadas
C1 = C2 = [[0 for i in range(10)] for i in range(10)]

class barco:

    vida = 0


# Creamos el mapa de juego. El parámetro i nos indica la longitud de eslora del barco,
# mientras que x es un objeto clase que representa un barco.

def dentro(a,b):
    if 0 <= a < 10 and 0 <= b < 10:
        return True
    return False


# Comprobamos si ninguna celda vecina está ocupada por un barco:  
# Necesitamos diferenciar si el barco estará en posición vertical u horizontal para 
# establecer los criterios en el momento de explorar las celdas vecinas

# Caso barco vertical
def vmira(M,a,b):
    for i in range(-1,2):
            if dentro(a-1,b-i):
                if M[a-1][b-i] != 'O':
                    return False
            if dentro(a,b-i):
                if M[a][b-i] != 'O':
                    return False
            if dentro(a+1,b-i):
                if M[a+1][b-i] != 'O':
                    return False
    return True


# Caso barco horizontal
def hmira(M,a,b):
    for i in range(-1,2):
        if dentro(a-i,b-1):
            if M[a-1][b-i] != 'O':
                return False
        if dentro(a-i,b):
            if M[a][b-i] != 'O':
                return False
        if dentro(a-i,b+1):
            if M[a-i][b+1] != 'O':
                return False
    return True



def valido(M,x,y,l,v):
    a = x
    b = y
    if v == True:
        for i in range(0,l):
            if not vmira(M,a,b):
                return False
        
    if v == False:
        for i in range(0,l):
            if not hmira(M,a,b):
                return False
        
    return True

def set_mapa(M, l, b):
    # el parámetro v nos indica si el barco que estamos colocando estará en posición vertical u horizontal
    v = random.randint(0,1)
    
    # Empezaremos a construir el barco eligiendo la primera casilla que este ocupará.
    # Si es vertical, la coordenada y (eje vertical) como máximo podrá ser 9 - l + 1, para evitar salirnos del mapa 
    if v == 1:
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9-l+1)
            if valido(M,x,y,l,v):
                break
        for i in range(0,l):
            M[x][y+i] = 'B'
            b.coord[str(x, int(y+i))] = False
    # Lo mismo ocurre si el barco está en posición horizontal, 
    # respectivamente con la variable x (eje horizontal)
    else:
        while True:
            x = random.randint(0,9-l+1)
            y = random.randint(0,9)
            if valido(M, x,y,l,v):
                break
        for i in range(0,l):
            M[x+i][y] = 'B'
            b.coord[str(int(x+i),y)] = False
    return M, b
#### DARLE UNA VUELTA!
flota = []
for l in range(1,5):
    for j in range(0,4-l):
        b = barco()
        M1, b = set_mapa(M1,l,b)
        flota.append(b)

b = barco()
b.coord

print(flota)
for i in range(len(M1)):
    for j in range(len(M1[i])):
        print(M1[i][j], end = " ")
    print("")
