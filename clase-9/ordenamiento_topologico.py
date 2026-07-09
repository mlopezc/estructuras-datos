from collections import defaultdict

class GrafoDirigido:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)

    def ordenamiento_topologico(self):
        visitados = set()
        pila = []

        def dfs(nodo):
            visitados.add(nodo)

            for vecino in self.grafo[nodo]:
                if vecino not in visitados:
                    dfs(vecino)

            pila.append(nodo)

        for nodo in list(self.grafo):
            if nodo not in visitados:
                dfs(nodo)

        return pila[::-1]


# Ejemplo
grafo = GrafoDirigido()
grafo.agregar_arista("Programar", "Probar")
grafo.agregar_arista("Diseñar", "Programar")
grafo.agregar_arista("Probar", "Entregar")
grafo.agregar_arista("Diseñar", "Documentar")
grafo.agregar_arista("Documentar", "Entregar")

print("Ordenamiento topológico:")
print(grafo.ordenamiento_topologico())