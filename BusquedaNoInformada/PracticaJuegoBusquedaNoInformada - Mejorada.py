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
            lista_hijos = []
            for i in range(0, (len(dato_nodo) - 1)):
                nodo_hijo = crear_hijo_por_par_de_indices(nodo, i, i + 1)
                lista_hijos.append(nodo_hijo)

            for hijo in lista_hijos:
                if (not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera)):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)


# crea un hijo intercambiando los valores de los índices pasados como argumentos
def crear_hijo_por_par_de_indices(nodo, pos_i, pos_f):
    arreglo = []
    for i in range(0, len(nodo.get_datos())):
        if i == pos_i:
            arreglo.append(nodo.get_datos()[pos_f])
        elif i == pos_f:
            arreglo.append(nodo.get_datos()[pos_i])
        else:
            arreglo.append(nodo.get_datos()[i])
    return Nodo(arreglo)


if __name__ == '__main__':

    estado_inicial = ['4', '6', '2', '3', '1', '5']
    solucion = ['1', '2', '3', '4', '5', '6']
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
