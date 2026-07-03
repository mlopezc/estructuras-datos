def dfs_iterativo(grafo, inicio):
    visitados = set()
    pila = [inicio]

    while pila:
        print("Pila actual:", pila)  # Mostrar el estado actual de la pila
        nodo = pila.pop()
        

        if nodo not in visitados:
            visitados.add(nodo)
            print("Nodos visitados:", visitados)
            print(nodo)

            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


dfs_iterativo(grafo, "A")