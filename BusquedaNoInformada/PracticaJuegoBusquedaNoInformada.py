'''
Created on 08/04/

@author: Mica
'''
from arbol import Nodo


def buscar_solucion_BFS(estado_inicial, solucion):
    # 1
    solucionado = False
    nodo_inicial = Nodo(estado_inicial)  # nodo inicial =  estado inicial
    nodos_frontera = []  # Nodos frontera = cola FIFO
    nodos_visitados = []  # Nodos visitados = Lista

    # 2
    nodos_frontera.append(nodo_inicial)  # Almacena el nodo inicial en la lista de nodos frontera

    print("Puntero:")
    # Mientras haya elementos en la lista de nodos frontera o se haya alcanzado la solucion
    while (not solucionado) and len(
            nodos_frontera) != 0:  # Mientras no este solucionado el problema y el nodo frontera no es vacio
        nodo = nodos_frontera.pop(0)  # Nodo Actual = extraer un nodo de la lista de nodos frotera
        nodos_visitados.append(nodo)  # Almaceno en la lista de nodos visitados
        print(nodo.get_datos())

        if nodo.get_datos() == solucion:  # Si el nodo actual es la solucion
            solucionado = True
            return nodo  # Retorno el nodo solucion o nodo objetivo
        else:

            # Expandir nodos hijos
            dato_nodo = nodo.get_datos()
            lista_hijos = [
                crear_hijo_por_izquierda(nodo),
                crear_hijo_por_centro(nodo),
                crear_hijo_por_derecha(nodo)
            ]

            for hijo in lista_hijos:
                if (not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera)):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)


def crear_hijo_por_izquierda(nodo):
    return Nodo([nodo.get_datos()[1], nodo.get_datos()[0], nodo.get_datos()[2], nodo.get_datos()[3]])


def crear_hijo_por_centro(nodo):
    return Nodo([nodo.get_datos()[0], nodo.get_datos()[2], nodo.get_datos()[1], nodo.get_datos()[3]])


def crear_hijo_por_derecha(nodo):
    return Nodo([nodo.get_datos()[0], nodo.get_datos()[1], nodo.get_datos()[3], nodo.get_datos()[2]])


if __name__ == '__main__':

    estado_inicial = ['4', '2', '3', '1']
    solucion = ['1', '2', '3', '4']
    nodo_solucion = buscar_solucion_BFS(estado_inicial,
                                        solucion)  # funcion encargada de implementar la busqueda

    resultado = []
    nodo = nodo_solucion

    # Para conocer el camino concreto del nodo raiz al nodo objetivo, solo hay que recorrer el camino inverso desde
    # el nodo objetvo
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)

    resultado.reverse()
    print("\nRecorrido:")
    print(resultado)
