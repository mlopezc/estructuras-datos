def floyd_warshall(grafo):
    vertices = list(grafo.keys())
    distancia = {}

    for i in vertices:
        distancia[i] = {}

        for j in vertices:
            if i == j:
                distancia[i][j] = 0
            elif j in grafo[i]:
                distancia[i][j] = grafo[i][j]
            else:
                distancia[i][j] = float("inf")

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distancia[i][k] + distancia[k][j] < distancia[i][j]:
                    distancia[i][j] = distancia[i][k] + distancia[k][j]

    return distancia


# Ejemplo
grafo = {
    "A": {"B": 3, "C": 8},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {"A": 2}
}

resultado = floyd_warshall(grafo)

print("Distancias mínimas entre todos los nodos:")

for origen in resultado:
    for destino in resultado[origen]:
        print(f"{origen} -> {destino}: {resultado[origen][destino]}")
    print()