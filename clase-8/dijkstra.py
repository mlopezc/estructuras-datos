import heapq

def dijkstra(grafo, inicio):
    distancias = {}

    for nodo in grafo:
        distancias[nodo] = float("inf")

    distancias[inicio] = 0

    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias


grafo_ponderado = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 1), ("D", 5)],
    "C": [("D", 8), ("E", 10)],
    "D": [("E", 2)],
    "E": []
}

resultado = dijkstra(grafo_ponderado, "A")
print(resultado)