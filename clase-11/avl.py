from node_tree import NodeTree


class AVLTree:
    """
    Árbol binario de búsqueda balanceado AVL.

    Después de cada inserción, el árbol verifica su factor
    de balance y realiza rotaciones cuando es necesario.
    """

    def __init__(self):
        self.root = None

    def height(self, node):
        """
        Calcula la altura de un nodo.
        """
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def balance_factor(self, node):
        """
        Factor de balance:

        altura izquierda - altura derecha
        """
        if node is None:
            return 0

        return self.height(node.left) - self.height(node.right)

    def insert(self, value):
        """
        Inserta un valor y balancea el árbol.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Inserción normal de un árbol binario de búsqueda
        if node is None:
            return NodeTree(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        else:
            # No se insertan valores repetidos
            return node

        # Se calcula el factor de balance
        balance = self.balance_factor(node)

        # Caso izquierda-izquierda
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Caso derecha-derecha
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Caso izquierda-derecha
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Caso derecha-izquierda
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def rotate_right(self, node):
        """
        Realiza una rotación simple hacia la derecha.

              y                 x
             / \               / \
            x   T3    ->       T1  y
           / \                   / \
          T1 T2                 T2 T3
        """
        new_root = node.left
        temporary_subtree = new_root.right

        new_root.right = node
        node.left = temporary_subtree

        return new_root

    def rotate_left(self, node):
        """
        Realiza una rotación simple hacia la izquierda.

            x                     y
           / \                   / \
          T1  y       ->        x  T3
             / \               / \
            T2 T3             T1 T2
        """
        new_root = node.right
        temporary_subtree = new_root.left

        new_root.left = node
        node.right = temporary_subtree

        return new_root

    def in_order(self):
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        if node is None:
            return

        self._in_order_recursive(node.left)
        print(node.value, end=" ")
        self._in_order_recursive(node.right)

    def pre_order(self):
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, node):
        if node is None:
            return

        print(node.value, end=" ")
        self._pre_order_recursive(node.left)
        self._pre_order_recursive(node.right)

    def print_tree(self):
        """
        Muestra el árbol horizontalmente.
        """
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level):
        if node is None:
            return

        self._print_tree_recursive(node.right, level + 1)

        print("    " * level + str(node.value))

        self._print_tree_recursive(node.left, level + 1)


if __name__ == "__main__":
    tree = AVLTree()

    values = [30, 20, 10, 25, 28, 27, 5, 40, 50, 45]

    for value in values:
        print(f"\nInsertando: {value}")
        tree.insert(value)
        tree.print_tree()

    print("\nRecorrido inorden:")
    tree.in_order()

    print("Recorrido preorden:")
    tree.pre_order()

    print("Altura final del árbol:", tree.height(tree.root))