import libros
import pprint

libros = libros.libros

def imprime(libros):
     pprint.pprint(libros)


def busca(libros):
    lib = input("Introduce el título del libro que deseas buscar:")
    lib = lib.strip().lower()
    encuentra = False
    for i in libros:
        if i["Titulo"].lower() == lib:
            print("Lo tenemos")
            encuentra = True
    if not encuentra:
        print("Lo sentimos, no lo tenemos")


def introduce(libros):
    tit = input("Introduce el título del libro")
    tit = tit.title().strip()
    aut = input("Introduce el autor del libro")
    aut = aut.title().strip()
    alq = input("¿Está alquilado? Responde sí o no")
    alq = alq.lower().strip()
    if alq == "sí" or alq == "si":
        alq = True
    else:
        alq = False        
    new = {"Titulo":tit, "Autor":aut, "Alquilado":alq}
    libros.append(new)
    print("Se ha añadido el libro a la libreria")
    

def elimina(libros):
    eli = input("¿Qué autor deseas eliminar?")
    eli = eli.title().strip()
    for n,i in enumerate(libros):
        if i["Autor"] == eli:
            del libros[n]

s = input("¿Qué acción deseas realizar? \n \
          Consultar todos los libros de la biblioteca \n \
          Buscar libro \n \
          aniadir libro \n \
          eliminar libro\n")
s.lower().strip()
match s:
    case "consultar todos los libros de la biblioteca":
        imprime(libros)
    case "buscar libro":
        busca(libros)
    case "aniadir libro":
        introduce(libros)
    case "eliminar libro":
        elimina(libros)
    case _:
        print("Acción no válida")
