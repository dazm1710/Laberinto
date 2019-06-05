class ArbolNario:
    def __init__(self, valor = ("", (0, 0)), hijos = []):
        self.valor = valor
        self.hijos = hijos



def abrir():
    return [x.strip("\n").split(" ") for x in open("laberinto.txt", "r").readlines()]

def EnLista(lista, valor):
    if lista == []:
        return False

    return lista[0] == valor or EnLista(lista[1:], valor)

def ListaDeListas(lista, v, f, c):
    if len(lista) == f:
        return [0, -1]

    if len(lista[f]) == c:
        return ListaDeListas(lista, v, f + 1, 0)

    if (lista[f][c] == v):
        return [f, c]

    return ListaDeListas(lista, v, f, c + 1)

def agregar(valor, lista):
    lista.append(valor)
    return lista

def arbol(lista, fc, lcoords):
    if fc[0] == len(lista) or fc[1] == len(lista[0]) or fc[0] < 0 or fc[1] < 0:
        return ArbolNario((" ", (fc[0], fc[0])), [])

    if EnLista(lcoords, (fc[0], fc[1])):
        return ArbolNario((lista[fc[0]][fc[1]], (fc[0], fc)[1]), [])

    if lista[fc[0]][fc[1]] == "1":
        return ArbolNario(("1", (fc[0], fc[1])), [])

    if lista[fc[0]][fc[1]] == "y":
        return ArbolNario(("y", (fc[0], fc[1])), [])

    if lista[fc[0]][fc[1]] == "0" or lista[fc[0]][fc[1]] == "x":    
        return ArbolNario((lista[fc[0]][fc[1]], (fc[0], fc[1])),[
                    arbol(lista, [fc[0],fc[1]+1], agregar((fc[0], fc[1]), lcoords)),
                    arbol(lista, [fc[0] + 1, fc[1]], agregar((fc[0], fc[1]), lcoords)),
                    arbol(lista, [fc[0], fc[1] - 1], agregar((fc[0], fc[1]), lcoords)),
                    arbol(lista, [fc[0] - 1, fc[1]], agregar((fc[0], fc[1]), lcoords))])

    print ("Solo 1,0,x,y")
    return ArbolNario(("Error: " + lista[fc[0]][fc[1]], (0, 0)), [])

def buscar(nodo, valor, camino):
    if nodo == None:
        return False

    if nodo.valor[0] == valor:
        camino.append(nodo.valor[1])
        return True

    if nodo.hijos == []:
        return False

    if buscar(nodo.hijos[0], valor, camino) or buscar(nodo.hijos[1], valor, camino)\
    or buscar(nodo.hijos[2], valor, camino) or buscar(nodo.hijos[3], valor, camino):
        camino.append(nodo.valor[1])
        return True

    return False


for x in abrir():
    print x
print ""
print("Existe un camino?: " + str(buscar(arbol(abrir(),ListaDeListas(abrir(), "x", 0, 0),[]),"y",[])))


