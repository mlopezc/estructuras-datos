class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}

    def find(self, vertice):
        if self.padre[vertice] != vertice:
            self.padre[vertice] = self.find(self.padre[vertice])
        return self.padre[vertice]

    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)

        if raiz_u != raiz_v:
            self.padre[raiz_v] = raiz_u
            return True

        return False


def kruskal(vertices, aristas):
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])
    union_find = UnionFind(vertices)

    mst = []
    costo_total = 0

    for u, v, peso in aristas_ordenadas:
        if union_find.union(u, v):
            mst.append((u, v, peso))
            costo_total += peso

    return mst, costo_total


# Ejemplo
vertices = ["A", "B", "C", "D", "E"]

aristas = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2)
]

mst, costo = kruskal(vertices, aristas)

print("Árbol de mínima expansión:")
for arista in mst:
    print(arista)

print("Costo total:", costo)