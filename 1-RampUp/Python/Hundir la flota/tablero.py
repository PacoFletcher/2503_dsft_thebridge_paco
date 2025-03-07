"""
LIBRERÍAS
"""

import random
import funciones

"""
CLASES
"""

class barco:
    
    def __init__(self):
        self.coord = {}
        self.vida = 0

class jugador:

    def __init__(self):
        self.vidas = 10
        self.flota = []
        self.mapa = []
        self.comprueba = []


# Creamos dos matrices, M1 y M2, que corresponderán a los mapas de cada jugador y una auxiliar para hacer las modificaciones
M = [['O' for i in range(10)] for i in range(10)]
M1 = [['O' for i in range(10)] for i in range(10)]
M2 = [['O' for i in range(10)] for i in range(10)]


# Creamos otras dos matrices, C1 y C2, que servirán a cada jugador para comprobar 
# las casillas ya visitadas
C1 = [[0 for i in range(10)] for i in range(10)]
C2 = [[0 for i in range(10)] for i in range(10)]


# Creamos el mapa de juego. El parámetro i nos indica la longitud de eslora del barco,
# mientras que x es un objeto clase que representa un barco.

def dentro(x,y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    return False

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


# Creamos una lista vacía, donde cada elemento sera un objeto clase barco
flota1 = []
# Crearemos uno por uno todos los barcos, por este motivo, los iremos implementando en el tablero según su longitud
# de eslora l
for l in range(1,5):
    # Cuanta menor sea la longitud de eslora, mayor será el número de barcos que implementaremos
    # Esto lo contabilizamos mediante el iterador j que va desde 0 a 5-l
    # En caso de l = 1, 4 barcos, l = 2, 3 barcos, etc. 
    for j in range(0,5-l):
        # Inicializamos un objeto barco y lo añadimos a nuestra lista
        b = barco()      
        flota1.append(b)
        # Ubicamos nuestro barco en el mapa del jugador:
        funciones.set_mapa(M1,l,flota1)

        # Implementamos este sistema de control que nos permite comprobar que
        # el programa se ejecuta correctamente 
        # una vez testeado, conviene comentar este bloque de código para 
        # disponer de una mejor presentación por pantalla
        """print(f"Barco de longitud {l} número {j}:")
        for i in range(len(M1)):
            for k in range(len(M1[i])):
                print(M1[i][k], end = " ")
            print("")"""

for i in flota1:
    print(i.vida, i.coord.items())

# print(flota)
for i in range(len(M1)):
    for j in range(len(M1[i])):
        print(M1[i][j], end = " ")
    print("")

# Reinicializamos la matriz auxiliar para completar el segundo mapa
M = [['O' for i in range(10)] for i in range(10)]

# Creamos una lista vacía, donde cada elemento sera un objeto clase barco
flota2 = []
# Crearemos uno por uno todos los barcos, por este motivo, los iremos implementando en el tablero según su longitud
# de eslora l
for l in range(1,5):
    # Cuanta menor sea la longitud de eslora, mayor será el número de barcos que implementaremos
    # Esto lo contabilizamos mediante el iterador j que va desde 0 a 5-l
    # En caso de l = 1, 4 barcos, l = 2, 3 barcos, etc. 
    for j in range(0,5-l):
        # Inicializamos un objeto barco y lo añadimos a nuestra lista
        b = barco()      
        flota2.append(b)
        # Ubicamos nuestro barco en el mapa del jugador:
        funciones.set_mapa(M2,l,flota2)

        # Implementamos este sistema de control que nos permite comprobar que
        # el programa se ejecuta correctamente 
        # una vez testeado, conviene comentar este bloque de código para 
        # disponer de una mejor presentación por pantalla
        """print(f"Barco de longitud {l} número {j}:")
        for i in range(len(M2)):
            for k in range(len(M2[i])):
                print(M2[i][k], end = " ")
            print("")"""
        

# Como esta información corresponde al segundo jugador (la máquina)
# no lo mostraremos en la versión definitiva
for i in flota2:
    print(i.vida, i.coord.items())

# print(flota)
for i in range(len(M2)):
    for j in range(len(M2[i])):
        print(M2[i][j], end = " ")
    print("")
