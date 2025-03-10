import jugada
import variables

while True:
    print("¡Bienvenido al juego de hundir la flota!")
    print("Antes de comenzar, debes seleccinar la dificultad de tu contrincante")
    dif = input("¿Cuál quieres que sea el nivel de dificultad?\n\
                0. La máquina realizará todas las tiradas de manera aleatoria.\n\
                1. La máquina intentará imitar la estrategia de un humano.\n\
                2. Si la máquina da con uno de tus barcos, puedes olvidarte de él.\n\
                3. ¡NI LO INTENTES! Este nivel es CASI imposible.\n")
    
    jugada(dif)
    
    otra = input("¿Quieres volver a jugar? ¿Sí o No?")
    otra = otra.lower()
    if otra != "sí" and otra != "si":
        break
print("Hasta la próxima")
