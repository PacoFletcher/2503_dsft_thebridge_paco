class barco:

    def __init__(self):
        self.coord = {(1,2): False}
        self.vidas = 0

lista = [(1,2), (3,3), (5,4)]


flota = []

for i in range(10):
    b = barco()
    flota.append(b)
    print(flota[-1].coord.items())
    print("EMPIEZA EL BUCLE")
    for j in lista:
        flota[-1].coord[j] = False
    print(f"Barco número {i}: {flota[-1].coord.items()}")
    print("")

for i in flota:
    print(i.vidas, i.coord.keys())



for i in lista:
    b.coord[i] = False 
b.vidas = len(b.coord.keys())
print(b.vidas)

for i,j in b.coord.items():
    print(i,j)
