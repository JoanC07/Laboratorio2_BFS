#Importamos la libreria Queve
from queue import Queue


class Grafo:
    # Constructor
    # Establecimiento de los parametros para el metodo constructor (inicializado)
    def __init__(self, numero_nodos, dirigido=True):
        '''Recibe el numero de nodos de nuestra clase principal Grafos - Constructor con parametros'''
        # Numero de nodos y creacion de rango de nodos
        self.m_numero_nodos = numero_nodos
        # Rango de nodos
        self.m_nodos = range(self.m_numero_nodos)

        # Tipo de grafo si es dirigida o no dirigida
        self.m_dirigido = dirigido

        # Representación gráfica - Lista de adyacencia
        # Usamos un directorio de datos para implementar una lista de adyacencia.
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

    # Agregar borde al gráfico
    def agregar_borde(self, nodo1, nodo2, peso=1):
        '''Recibe los nodos1 y nodo2 ademas del peso y se agregan a nuestra lista de
         adyacencia con el nodo que corresponde'''
        #Agrega el nodo 2 a nuestra lista del nodo 1
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))

        if not self.m_dirigido:
            #Agrega el nodo 1 a nuestra lista del nodo 2
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    # Imprimir la representación gráfica
    def Imprimir_lista_adyacencia(self):
        '''Nos imprime por pantalla el grafo generado nuestra lista de ayacencia, no rebibe parametros'''
        #Recorre la lista
        for llave in self.m_lista_adyacencia.keys():
            #Imprime nuestro nodo
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

        # Función que imprime el recorrido BFS de un vértice fuente dado. bfs_traversal(int s)
        # recorre los vértices alcanzables desde s.
    def bfs_transversal(self, nodo_de_inicio):
        '''Genera una lista de las colas visitadas y muestra el recorrido realizado, recibe el 
        valor de nodo_de_inicio.'''
        # Conjunto de nodos visitados para evitar bucles
        visitado = set()
        cola = Queue()

        # Añade el nodo_de_inicio a la cola y a la lista de visitas
        cola.put(nodo_de_inicio)
        visitado.add(nodo_de_inicio)

        #Bucle de los nodos
        while not cola.empty():
            # Quitar un vértice de la cola
            nodo_actual = cola.get()  
            # Imprimirlo vertice
            print(nodo_actual, end=" ")  

            # Obtener todos los vértices adyacentes del
            # vértice de la cola. 
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
              #Si un vértice adyacente ha sido visitado, entonces se marca como visitado y pongalo en cola
                if siguiente_nodo not in visitado:
                    cola.put(siguiente_nodo)
                    visitado.add(siguiente_nodo)


if __name__ == "__main__":
   
    # Se crea la instancia de la clase `Grafo`.
    # Tiene 5 nodos y es no dirigido
    g = Grafo(5, dirigido = False)
    # Cuantos nodos va a tener (nodo maximo) 0-3
    # Estados y peso (costo hacer referenia al Ejemplo de los canibales)
    #Agrega los bordes a nuestro Grafo
    g.agregar_borde(3, 1)
    g.agregar_borde(2, 2)
    g.agregar_borde(1, 4)
    g.agregar_borde(0, 4)
    g.agregar_borde(2, 3)

    # Imprime la lista de adyacencia en la forma nodo n: {(nodo, peso)}
    g.Imprimir_lista_adyacencia()

    print("A continuación se muestra el recorrido primero en anchura"
          " (a partir del vértice 0)")
    #Imprime toda la lista de colas
    g.bfs_transversal(0)
    print()