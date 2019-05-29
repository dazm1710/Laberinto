from array import *

laberinto = [x.split() for x in open("laberinto.txt","r").readlines()]


#Para el arbol
class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der



def encontrar(lista,arbol):
    if(arbol.valor=='y'):
        return true
    #if(arbol==None):
    


def rotar(lista):
    if len(lista)>=2:
        return list(reversed(map(list, zip(*reversed(lista[::-1])))))
    return lista

def encontrarX(lista):
    if lista==[]:
        return "No esta x"
    if recorrer(lista[0]):
        return "encontrada"
    return encontrarX(rotar(lista[1:]))


def recorrer(renglon):
    if len(renglon)==0:
        return False
    print renglon[0]
    if(renglon[0]=="x"):
        return True
    return recorrer(renglon[1:])


print encontrarX(laberinto)
#print recorrer(renglon)
"""
print laberinto
"""
