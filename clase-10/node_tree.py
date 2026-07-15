class NodeTree:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def mostrar(self, nivel=0):
        sangria = "  " * nivel
        print(f"{sangria}- {self.valor}")

        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)


