import tablero
import os

turno = 0
tirada = 1
vidas = [20,20]

os.system('tablero.py')

#exec(open("tablero.py").read())


P = [tablero.M1.copy(), tablero.M2.copy()]

Q = [tablero.C1.copy(), tablero.C2.copy()]

R = [tablero.flota1.copy(),tablero.flota2.copy()]

