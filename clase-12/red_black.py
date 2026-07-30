
RED = "RED"
BLACK = "BLACK"


class RedBlackNode:
    """
    Nodo de un Red-Black Tree.
    """

    def __init__(self, value=None, color=RED):
        self.value = value
        self.color = color

        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"{self.value} ({self.color})"


class RedBlackTree:
    """
    Árbol binario de búsqueda Red-Black.
    """

    def __init__(self):
        # Nodo centinela utilizado en lugar de None
        self.nil = RedBlackNode(color=BLACK)

        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil

        self.root = self.nil

    def insert(self, value):
        """
        Inserta un valor y restaura las propiedades Red-Black.
        """

        new_node = RedBlackNode(value=value, color=RED)

        new_node.left = self.nil
        new_node.right = self.nil
        new_node.parent = self.nil

        parent = self.nil
        current = self.root

        # Inserción normal de un árbol binario de búsqueda
        while current != self.nil:
            parent = current

            if new_node.value < current.value:
                current = current.left
            elif new_node.value > current.value:
                current = current.right
            else:
                # No se insertan duplicados
                return

        new_node.parent = parent

        if parent == self.nil:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # Si es la raíz, debe ser negra
        if new_node.parent == self.nil:
            new_node.color = BLACK
            return

        # Si el padre es la raíz, no hay violación
        if new_node.parent.parent == self.nil:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        """
        Corrige las violaciones producidas por una inserción.
        """

        while node.parent.color == RED:

            # El padre está a la derecha del abuelo
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left

                # Caso 1: el tío es rojo
                if uncle.color == RED:
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED

                    node = node.parent.parent

                else:
                    # Caso 2: el nodo está a la izquierda
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)

                    # Caso 3: el nodo está a la derecha
                    node.parent.color = BLACK
                    node.parent.parent.color = RED

                    self._rotate_left(node.parent.parent)

            # El padre está a la izquierda del abuelo
            else:
                uncle = node.parent.parent.right

                # Caso 1: el tío es rojo
                if uncle.color == RED:
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED

                    node = node.parent.parent

                else:
                    # Caso 2: el nodo está a la derecha
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)

                    # Caso 3: el nodo está a la izquierda
                    node.parent.color = BLACK
                    node.parent.parent.color = RED

                    self._rotate_right(node.parent.parent)

            if node == self.root:
                break

        self.root.color = BLACK

    def _rotate_left(self, node):
        """
        Rotación hacia la izquierda.
        """

        new_root = node.right

        node.right = new_root.left

        if new_root.left != self.nil:
            new_root.left.parent = node

        new_root.parent = node.parent

        if node.parent == self.nil:
            self.root = new_root

        elif node == node.parent.left:
            node.parent.left = new_root

        else:
            node.parent.right = new_root

        new_root.left = node
        node.parent = new_root

    def _rotate_right(self, node):
        """
        Rotación hacia la derecha.
        """

        new_root = node.left

        node.left = new_root.right

        if new_root.right != self.nil:
            new_root.right.parent = node

        new_root.parent = node.parent

        if node.parent == self.nil:
            self.root = new_root

        elif node == node.parent.right:
            node.parent.right = new_root

        else:
            node.parent.left = new_root

        new_root.right = node
        node.parent = new_root

    def search(self, value):
        """
        Busca un valor en el árbol.
        """

        current = self.root

        while current != self.nil:

            if value == current.value:
                return current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def in_order(self):
        """
        Retorna los valores ordenados junto con su color.
        """

        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node == self.nil:
            return

        self._in_order_recursive(node.left, result)

        result.append(
            f"{node.value} ({node.color})"
        )

        self._in_order_recursive(node.right, result)

    def level_order(self):
        """
        Retorna los nodos por niveles.
        """

        if self.root == self.nil:
            return []

        queue = [self.root]
        result = []

        while queue:
            current = queue.pop(0)

            result.append(
                f"{current.value} ({current.color})"
            )

            if current.left != self.nil:
                queue.append(current.left)

            if current.right != self.nil:
                queue.append(current.right)

        return result

    def print_tree(self):
        """
        Muestra el árbol horizontalmente.
        """

        self._print_recursive(self.root, "", True)

    def _print_recursive(self, node, indentation, last):
        if node == self.nil:
            return

        print(indentation, end="")

        if last:
            print("R----", end="")
            indentation += "     "
        else:
            print("L----", end="")
            indentation += "|    "

        print(f"{node.value} ({node.color})")

        self._print_recursive(
            node.left,
            indentation,
            False
        )

        self._print_recursive(
            node.right,
            indentation,
            True
        )


if __name__ == "__main__":
    tree = RedBlackTree()

    values = [
        55, 40, 65, 60, 75,
        57, 20, 35, 50, 10
    ]

    for value in values:
        print(f"\nInsertando {value}")
        tree.insert(value)

    print("\nRed-Black Tree:")
    tree.print_tree()

    print("\nRecorrido inorden:")
    print(tree.in_order())

    print("\nRecorrido por niveles:")
    print(tree.level_order())

    value_to_search = 57
    result = tree.search(value_to_search)

    if result:
        print(
            f"\nValor encontrado: "
            f"{result.value} ({result.color})"
        )
    else:
        print(f"\nEl valor {value_to_search} no existe.")