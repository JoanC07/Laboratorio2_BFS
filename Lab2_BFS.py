'''Importamos la libreria Queve'''
from queue import Queue

class Grafo:
    '''
    Clase Grafo la cual nos va a representar a nuestro Grafo.

    ...

    Parametros
    ----------
        m_numero_nodos : int
            Numero de nodos 
        numero_nodos : int
            Rango de nodos 
        m_dirigido : boolean
            Tipo de grafo si es dirigida o no dirigida.
        m_lista_adyacencia : diccionario
            Representación gráfica - Lista de adyacencia.
    Establecimiento de los parametros para el metodo constructor (inicializado)

    Métodos
    ------- 
        Agregar_borde(self, nodo1, nodo2, peso=1):
            Agregar arista al grafo.
        Imprimir_lista_adyacencia(self):
            Imprime la representacion grafica
        __init__(self, numero_nodos, dirigido=True):
            Recibe el numero de nodos y rango y verifica si es dirigido o no
        bfs_transversal(nodo_inicial):
            Imprimir el recorrido BFS de un vértice fuente dado.

    '''
    def __init__(self, numero_nodos, dirigido=True):
        '''
        Recibe el numero de nodos de nuestra clase principal Grafos. 

        Parametros.
            m_numero_nodos : int
                 Numero de nodos 
            numero_nodos : int
                Rango de nodos 
            m_dirigido : boolean
                Tipo de grafo si es dirigida o no dirigida.
            m_lista_adyacencia : diccionario
                Representación gráfica - Lista de adyacencia.
        '''
        # Numero de nodos 
        self.m_numero_nodos = numero_nodos
        # Rango de nodos
        self.m_nodos = range(self.m_numero_nodos)
        # Tipo de grafo si es dirigida o no dirigida
        self.m_dirigido = dirigido
        # Usamos un directorio de datos para implementar una lista de adyacencia.
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

    def agregar_borde(self, nodo1, nodo2, peso=1):
        '''
        Agregar borde al gráfo. 
        Parametros.
        ----------
            nodo1: int
            nodo2: int
            peso: int
            Peso y se agregan a nuestra lista de adyacencia con el nodo que corresponde.
        '''
        #Agrega el nodo 2 a nuestra lista del nodo 1
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        if not self.m_dirigido:
            #Agrega el nodo 1 a nuestra lista del nodo 2
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    # Imprimir la representación gráfica
    def Imprimir_lista_adyacencia(self):
        '''
        Nos imprime la representacion grafica por pantalla el grafo generado nuestra lista de ayacencia.

        Parametros.
        ---------- 
        No recibe.

        Retorna.
        ------
        Nada.
        '''
        #Recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            #Imprime nuestro nodo
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def bfs_transversal(self, nodo_de_inicio):
        '''
        Función que imprime el recorrido BFS de un vértice fuente dado. bfs_traversal(int s) y
        recorre los vértices alcanzables desde s.
        Genera una lista de las colas visitadas y muestra el recorrido realizado, recibe el 
        valor de nodo_de_inicio.

        Parametros
        -----------
        nodo_de_inicio : int

        Retorna
        -------
        Recorido del nodo


         Añade el nodo_de_inicio a la cola y a la lista de visitas.

        Bucle de los nodos.
            Quitar un vértice de la cola.
            Imprimirlo vertice.
            Obtener todos los vértices adyacentes del vértice de la cola. 
                    Si un vértice adyacente ha sido visitado, entonces se marca como visitado y pongalo en cola.
        '''
        # Conjunto de nodos visitados para evitar bucles
        visitado = set()
        cola = Queue()
        # Añade el nodo_de_inicio a la cola 
        cola.put(nodo_de_inicio)
        # Agrega a la lista de visitas
        visitado.add(nodo_de_inicio)
        #Bucle de los nodos
        while not cola.empty():
            # Quitar un vértice de la cola
            nodo_actual = cola.get()  
            # Imprimirlo vertice
            print(nodo_actual, end=" ")  
            # Obtener todos los vértices adyacentes de la cola. 
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
              #Si un vértice adyacente ha sido visitado
                if siguiente_nodo not in visitado:
                    #Se coloca en la cola
                    cola.put(siguiente_nodo)
                    #Se marca el nodo
                    visitado.add(siguiente_nodo)

if __name__ == "__main__":

    '''
    Se crea la instancia de la clase `Grafo`. 
    Nodo de 5 y no es dirigido Grafo(5, dirigido = False).
    Cantidad de nodos va a tener y agrega bordes a nuestro Grafo (3, 1).
    Imprime la lista de adyacencia en la forma nodo n: {(nodo, peso)} e imprime la lista de colas. 
    '''
    print("----------------------------------------------------------")
    print("Caso 1")
    grafo1 = Grafo(5, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo1.agregar_borde(3, 1)
    grafo1.agregar_borde(2, 2)
    grafo1.agregar_borde(1, 4)
    grafo1.agregar_borde(0, 2)
    grafo1.agregar_borde(2, 3)

    # Imprime la lista de colas
    grafo1.Imprimir_lista_adyacencia()

    print("A continuación se muestra el recorrido primero en anchura"
          " (a partir del vértice 0).")

    grafo1.bfs_transversal(0)
    print()

    print("----------------------------------------------------------")
    print("Caso 2")
    grafo2 = Grafo(4, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo2.agregar_borde(2, 1)
    grafo2.agregar_borde(1, 2)
    grafo2.agregar_borde(0, 2)
    grafo2.agregar_borde(3, 3)

    # Imprime la lista de colas
    grafo2.Imprimir_lista_adyacencia()

    print("A continuación se muestra el recorrido primero en anchura"
          " (a partir del vértice 0).")

    # Imprime toda la lista de colas.

    grafo2.bfs_transversal(0)
    print()

    print("----------------------------------------------------------")
    print("Caso 3")
    grafo3 = Grafo(5, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo3.agregar_borde(2, 0)
    grafo3.agregar_borde(4, 2)
    grafo3.agregar_borde(1, 4)
    grafo3.agregar_borde(0, 3)
    grafo3.agregar_borde(3, 1)

    # Imprime la lista de colas
    grafo3.Imprimir_lista_adyacencia()

    print("A continuación se muestra el recorrido primero en anchura"
          " (a partir del vértice 0).")

    grafo3.bfs_transversal(0)
    print()

    print("----------------------------------------------------------")
    print("Caso 4")
    grafo4 = Grafo(6, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo4.agregar_borde(2, 1)
    grafo4.agregar_borde(5, 2)
    grafo4.agregar_borde(3, 4)
    grafo4.agregar_borde(0, 5)
    grafo4.agregar_borde(2, 2)
    grafo4.agregar_borde(1, 3)

    # Imprime la lista de colas
    grafo4.Imprimir_lista_adyacencia()

    print("A continuación se muestra el recorrido primero en anchura"
          " (a partir del vértice 0).")

    grafo4.bfs_transversal(0)
    print()

    print("----------------------------------------------------------")
    print("Caso 5")
    grafo5 = Grafo(7, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo5.agregar_borde(1, 3)
    grafo5.agregar_borde(2, 2)
    grafo5.agregar_borde(5, 4)
    grafo5.agregar_borde(0, 5)
    grafo5.agregar_borde(3, 1)
    grafo5.agregar_borde(6, 0)
    grafo5.agregar_borde(4, 6)

    # Imprime la lista de colas
    grafo5.Imprimir_lista_adyacencia()

    print("A continuación se muestra el recorrido primero en anchura"
          " (a partir del vértice 0).")

    grafo5.bfs_transversal(0)
    print()
