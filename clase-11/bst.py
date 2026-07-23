from node_tree import NodeTree


class BinarySearchTree:
    """
    Árbol binario de búsqueda.

    Los valores menores se almacenan a la izquierda.
    Los valores mayores se almacenan a la derecha.
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserta un valor en el árbol.
        """
        if self.root is None:
            self.root = NodeTree(value)
            return

        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return NodeTree(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        else:
            print(f"El valor {value} ya existe en el árbol.")

        return node

    def search(self, value):
        """
        Busca un valor en el árbol.

        Retorna el nodo encontrado o None.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return None

        if value == node.value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def in_order(self):
        """
        Muestra los valores de menor a mayor.
        """
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        if node is None:
            return

        self._in_order_recursive(node.left)
        print(node.value, end=" ")
        self._in_order_recursive(node.right)

    def find_minimum(self):
        """
        Retorna el menor valor del árbol.
        """
        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.value

    def find_maximum(self):
        """
        Retorna el mayor valor del árbol.
        """
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.value

    def delete(self, value):
        """
        Elimina un valor del árbol.
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)

        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)

        else:
            # Caso 1: nodo sin hijo izquierdo
            if node.left is None:
                return node.right

            # Caso 2: nodo sin hijo derecho
            if node.right is None:
                return node.left

            # Caso 3: nodo con dos hijos
            successor = self._find_minimum_node(node.right)
            node.value = successor.value

            node.right = self._delete_recursive(
                node.right,
                successor.value
            )

        return node

    def _find_minimum_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current


if __name__ == "__main__":
    tree = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    print("Árbol recorrido en inorden:")
    tree.in_order()

    value_to_search = 60
    result = tree.search(value_to_search)

    if result is not None:
        print(f"El valor {value_to_search} fue encontrado.")
    else:
        print(f"El valor {value_to_search} no existe.")

    print("Valor mínimo:", tree.find_minimum())
    print("Valor máximo:", tree.find_maximum())

    print("\nEliminando el valor 30...")
    tree.delete(30)

    print("Árbol después de eliminar:")
    tree.in_order()