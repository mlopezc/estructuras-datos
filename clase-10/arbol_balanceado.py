class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0

        return nodo.altura

    def obtener_balance(self, nodo):
        if nodo is None:
            return 0

        return (
            self.obtener_altura(nodo.izquierdo)
            - self.obtener_altura(nodo.derecho)
        )

    def rotar_derecha(self, nodo_desbalanceado):
        nueva_raiz = nodo_desbalanceado.izquierdo
        subarbol_temporal = nueva_raiz.derecho

        nueva_raiz.derecho = nodo_desbalanceado
        nodo_desbalanceado.izquierdo = subarbol_temporal

        nodo_desbalanceado.altura = 1 + max(
            self.obtener_altura(nodo_desbalanceado.izquierdo),
            self.obtener_altura(nodo_desbalanceado.derecho)
        )

        nueva_raiz.altura = 1 + max(
            self.obtener_altura(nueva_raiz.izquierdo),
            self.obtener_altura(nueva_raiz.derecho)
        )

        return nueva_raiz

    def rotar_izquierda(self, nodo_desbalanceado):
        nueva_raiz = nodo_desbalanceado.derecho
        subarbol_temporal = nueva_raiz.izquierdo

        nueva_raiz.izquierdo = nodo_desbalanceado
        nodo_desbalanceado.derecho = subarbol_temporal

        nodo_desbalanceado.altura = 1 + max(
            self.obtener_altura(nodo_desbalanceado.izquierdo),
            self.obtener_altura(nodo_desbalanceado.derecho)
        )

        nueva_raiz.altura = 1 + max(
            self.obtener_altura(nueva_raiz.izquierdo),
            self.obtener_altura(nueva_raiz.derecho)
        )

        return nueva_raiz

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        # Inserción normal de un árbol binario de búsqueda
        if nodo is None:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(
                nodo.izquierdo,
                valor
            )
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(
                nodo.derecho,
                valor
            )
        else:
            # No se insertan valores repetidos
            return nodo

        # Actualizar la altura del nodo
        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierdo),
            self.obtener_altura(nodo.derecho)
        )

        # Calcular el factor de balance
        balance = self.obtener_balance(nodo)

        # Caso izquierda-izquierda
        if balance > 1 and valor < nodo.izquierdo.valor:
            return self.rotar_derecha(nodo)

        # Caso derecha-derecha
        if balance < -1 and valor > nodo.derecho.valor:
            return self.rotar_izquierda(nodo)

        # Caso izquierda-derecha
        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)

        # Caso derecha-izquierda
        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)

        return nodo

    def mostrar_inorden(self):
        self._mostrar_inorden_recursivo(self.raiz)
        print()

    def _mostrar_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._mostrar_inorden_recursivo(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self._mostrar_inorden_recursivo(nodo.derecho)

    def mostrar_estructura(self):
        self._mostrar_estructura_recursiva(self.raiz)

    def _mostrar_estructura_recursiva(
        self,
        nodo,
        prefijo="",
        es_izquierdo=True
    ):
        if nodo is None:
            return

        if nodo.derecho is not None:
            self._mostrar_estructura_recursiva(
                nodo.derecho,
                prefijo + ("│   " if es_izquierdo else "    "),
                False
            )

        print(
            prefijo
            + ("└── " if es_izquierdo else "┌── ")
            + str(nodo.valor)
        )

        if nodo.izquierdo is not None:
            self._mostrar_estructura_recursiva(
                nodo.izquierdo,
                prefijo + ("    " if es_izquierdo else "│   "),
                True
            )


# Ejemplo de uso
arbol_avl = ArbolAVL()

valores = [10, 20, 30, 40, 50, 25]

for valor in valores:
    arbol_avl.insertar(valor)

print("Recorrido inorden:")
arbol_avl.mostrar_inorden()

print("\nEstructura del árbol AVL:")
arbol_avl.mostrar_estructura()