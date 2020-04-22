'''
Created on 08/04/

@author: Mica
'''
from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    
    #1
    solucionado = False
    nodo_inicial = Nodo(estado_inicial) #nodo inicial =  estado inicial 
    nodos_frontera = [] #Nodos frontera = cola FIFO
    nodos_visitados = [] # Nodos visitados = Lista

    #2
    nodos_frontera.append(nodo_inicial) # Almacena el nodo inicial en la lista de nodos frontera

    print("Puntero:")
    #Mientras haya elementos en la lista de nodos frontera o se haya alcanzado la solucion
    while (not solucionado) and len(nodos_frontera) != 0:  #Mientras no este solucionado el problema y el nodo frontera no es vacio
        nodo = nodos_frontera.pop()  #Nodo Actual = extraer un nodo de la lista de nodos frotera
        nodos_visitados.append(nodo) #Almaceno en la lista de nodos visitados
        print(nodo.get_datos())

        if nodo.get_datos() == solucion:  #Si el nodo actual es la solucion
            solucionado = True  
            return nodo #Retorno el nodo solucion o nodo objetivo
        else:

            #Expandir nodos hijos, nodos con conexion
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if(not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera)):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

            
if __name__ == '__main__':
    conexiones = {
        'A':{'D','F','G'},
        'D':{'A','H','J'},
        'H':{'D','B'},
        'B':{'H'},
        'J':{'D','K'},
        'K':{'J','L'},
        'L':{'K'},
        'F':{'C','A','E'},
        'C':{'F'},
        'E':{'F','Z','W'},
        'Z':{'E'},
        'W':{'E'},
        'G':{'A'}
        }
    estado_inicial = str('A')
    solucion =  str('B')
    nodo_solucion = buscar_solucion_BFS(conexiones,estado_inicial, solucion) #funcion encargada de implementar la busqueda

    resultado = []
    nodo = nodo_solucion
    
    #Para conocer el camino concreto del nodo raiz al nodo objetivo, solo hay que recorrer el camino inverso desde
    #el nodo objetvo 
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)

    resultado.reverse()
    print ("Recorrido:")
    print (resultado)