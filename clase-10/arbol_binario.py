class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def mostrar_preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self.mostrar_preorden(nodo.izquierdo)
            self.mostrar_preorden(nodo.derecho)

    def mostrar_inorden(self, nodo):
        if nodo is not None:
            self.mostrar_inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.mostrar_inorden(nodo.derecho)

    def mostrar_postorden(self, nodo):
        if nodo is not None:
            self.mostrar_postorden(nodo.izquierdo)
            self.mostrar_postorden(nodo.derecho)
            print(nodo.valor, end=" ")


# Crear el árbol
arbol = ArbolBinario()

arbol.raiz = NodoBinario("A")
arbol.raiz.izquierdo = NodoBinario("B")
arbol.raiz.derecho = NodoBinario("C")

arbol.raiz.izquierdo.izquierdo = NodoBinario("D")
arbol.raiz.izquierdo.derecho = NodoBinario("E")

arbol.raiz.derecho.izquierdo = NodoBinario("F")
arbol.raiz.derecho.derecho = NodoBinario("G")

print("Preorden:")
arbol.mostrar_preorden(arbol.raiz)

print("\nInorden:")
arbol.mostrar_inorden(arbol.raiz)

print("\nPostorden:")
arbol.mostrar_postorden(arbol.raiz)