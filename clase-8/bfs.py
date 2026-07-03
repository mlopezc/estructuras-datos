from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque()

    visitados.add(inicio)
    cola.append(inicio)

    while cola:
        print("Cola actual:", list(cola))   
        nodo = cola.popleft()
        print(nodo)

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    print("Nodos visitados:", visitados)

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

bfs(grafo, "A")