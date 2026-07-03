def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(nodo)
    print(nodo)

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

dfs(grafo, "A")