import random
import variables
"""
turno = variables.turno
tirada = variables.tirada
vidas = variables.vidas

M = variables.M
C = variables.C
F = variables.F

"""

def dentro(x,y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    return False


def imprime_tablero(C):
    for i in range(-1,10):
        if i == -1:
            print (" ", end = " | ")
        else:
            print(i, end = " | ")
    print("")
    print("-"*43)
    for i in range(len(C)):
        for j in range(len(C[i])+1):
            if j == 0:
                print(i, end  = " | ")
            else:
                print(C[i][j-1], end = " | ")
        print("")
        print("-"*43)


def disparo(M,C,F,x,y,turno):
    t = (turno+1)%2
    if dentro(x,y) and C[turno][x][y] == 0:
        if M[t][x][y] == 'O':
            C[turno][x][y] = 'A'
            print(f"Coordenada ({x},{y}): Agua. Turno del otro jugador")
            turno += 1
            acierto = False
            return turno, acierto
        else:
            C[turno][x][y] = 'T'
            k = (x,y)
            aux = 0
            print("El valor t es: ", t)
            for i in range(len(F[t])):
                if k in F[t][i].coord.keys():
                    F[t][i].coord[k] = True
                    F[t][i].vida -= 1
                    aux = i
            if F[t][aux].vida == 0:
                print(f"Coordenada ({x},{y}): Tocado y hundido. Vuelve a tirar")
                
                C[turno] = pinta(C,F[t][aux])
            else:
                print(f"Coordenada ({x},{y}): Tocado. Vuelve a tirar")
            vidas[t] -= 1
    else:
        print(f"Coordenada ({x},{y}) fuera del tablero o ya visitada, prueba otra combinación")

def tira1(M,C,F,turno):
    x = int(input("Introduce la primera coordenada de la tirada:"))
    y = int(input("Introduce la segunda coordenada de la tirada:"))
    turno, acierto = disparo(M,C,F,x,y,turno) 
    return turno, acierto
    """
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
    """

### Aquí irán las diferentes dificultades de la máquina:


### (Dummy) Todas las tiradas serán aleatorias
"""
def dif_0(C):

"""
### (Nivel 1) Las tiradas serán aleatorias, pero en caso de tocar
### un barco, las siguientes tiradas las hará en el entorno de la casilla
### hasta hundirlo 
"""
def dif_1(C):

"""

### (Nivel 2) Similar al nivel 1, sólo que las próximas tiradas sólo las efectuará si sabe que hay un barco.
### Es decir, si toca un barco, en el mismo turno lo hundirá.

"""
def dif_2(C):

"""

### (Nivel 3) Nivel (casi) imposible.
### La máquina accede a nuestro vector flota, por lo que en un solo turno hundirá todos nuestros barcos

"""
def dif_3(C):

"""

def pinta(C,b):
    for i in b.coord.keys():
        x = i[0]
        y = i[1]
        for j in range(-1,2):
            for k in range(-1,2):
                if dentro(x-j,y-k):
                    C[x-j][y-k] = "X"
    return C
                

# Función reservada para las jugadas.
# Comprueba si las coordenadas de la tirada son válidas y si ya las hemos visitado
def comprueba(C,x,y):
    if dentro(x,y):
        if C[x][y] != 0:
            return False
    else:
        return False
    return True
# Comprobamos si ninguna celda vecina está ocupada por un barco:  

# Para cada celda que ocupará nuestro barco, miramos ésta misma junto con sus 8 celdas vecinas
def mira(M,x,y):
    for i in range(-1,2):
            for j in range(-1,2):
                if dentro(x-j,y-i):
                    if M[x-j][y-i] != 'O':
                        return False
    return True

# En este caso, caemos en cierta redundancia, ya que al avanzar
# en las casillas candidatas a ser ocupadas por un mismo barco
# analizamos repetidamente algunas que se solapan.
# Como todavía no estamos modificando el mapa, esto no crea ningún conflico,
# por lo que sacrificamos un poco de eficiencia computacional a cambio de limpieza de código


# Función descartada debido a redundancia
"""
# Caso barco horizontal
def hmira(M,x,y):
    for i in range(-1,2):
        if dentro(x-i,y-1):
            if M[x-i][y-1] != 'O':
                return False
        if dentro(x-i,y):
            if M[x-i][y] != 'O':
                return False
        if dentro(x-i,y+1):
            if M[x-i][y+1] != 'O':
                return False
    return True
"""

# En esta función comprobaremos si las celdas que se asignarán al barco
# cumplen los requisitos establecidos:
# 1. Ninguna de ellas está ocupada por otro barco
# 2. Ninguna celda vecina está ocupada por otro barco
def valido(M,x,y,l,v):
    # Analizaremos celda a celda.
    # Si el barco está en posición vertical, modificaremos la coordenada x 
    if v == True:
        for i in range(0,l):
            if not mira(M,x+i,y):
                return False
    # Si el barco está en posición horizontal, modificaremos la coordenada y    
    if v == False:
        for i in range(0,l):
            if not mira(M,x,y+i):
                return False
        
    return True

def set_mapa(M, l, flota):
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
            M[x+i][y] = 'B'
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
            M[x][y+i] = 'B'
            t = (x,y+i)
            flota[-1].coord[t] = False
        flota[-1].vida = len(flota[-1].coord.keys())
