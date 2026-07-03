def bellman_ford(vertices, aristas, inicio):
    distancias = {}

    for vertice in vertices:
        distancias[vertice] = float("inf")

    distancias[inicio] = 0

    # Relajar todas las aristas V - 1 veces
    for _ in range(len(vertices) - 1):
        for origen, destino, peso in aristas:
            if distancias[origen] + peso < distancias[destino]:
                distancias[destino] = distancias[origen] + peso

    # Verificar si existe un ciclo negativo
    for origen, destino, peso in aristas:
        if distancias[origen] + peso < distancias[destino]:
            print("El grafo contiene un ciclo negativo")
            return None

    return distancias


vertices = ["A", "B", "C", "D", "E"]

aristas = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", -1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("D", "E", 2)
]

resultado = bellman_ford(vertices, aristas, "A")
print(resultado)