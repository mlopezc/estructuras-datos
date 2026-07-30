class BTreeNode:
    """
    Nodo de un B-Tree.

    Cada nodo puede almacenar múltiples claves
    y múltiples referencias a hijos.
    """

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    """
    Implementación de un B-Tree.

    t representa el grado mínimo del árbol.

    Cantidad máxima de claves por nodo:
        2 * t - 1

    Cantidad máxima de hijos por nodo:
        2 * t
    """

    def __init__(self, minimum_degree=2):
        if minimum_degree < 2:
            raise ValueError("El grado mínimo debe ser al menos 2.")

        self.t = minimum_degree
        self.root = BTreeNode(leaf=True)

    def search(self, key, node=None):
        """
        Busca una clave en el árbol.

        Retorna una tupla:
            (nodo, posición)

        Si no encuentra la clave, retorna None.
        """

        if node is None:
            node = self.root

        index = 0

        # Busca la primera clave mayor o igual a key
        while index < len(node.keys) and key > node.keys[index]:
            index += 1

        # La clave fue encontrada
        if index < len(node.keys) and key == node.keys[index]:
            return node, index

        # Si es una hoja, la clave no existe
        if node.leaf:
            return None

        # Continúa la búsqueda en el hijo correspondiente
        return self.search(key, node.children[index])

    def insert(self, key):
        """
        Inserta una clave en el árbol.
        """

        root = self.root
        maximum_keys = 2 * self.t - 1

        # Si la raíz está llena, se debe dividir
        if len(root.keys) == maximum_keys:
            new_root = BTreeNode(leaf=False)

            new_root.children.append(root)
            self.root = new_root

            self._split_child(new_root, 0)
            self._insert_non_full(new_root, key)

        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        """
        Inserta una clave en un nodo que no está lleno.
        """

        index = len(node.keys) - 1

        if node.leaf:
            # Agrega espacio para la nueva clave
            node.keys.append(None)

            # Desplaza las claves mayores hacia la derecha
            while index >= 0 and key < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1

            node.keys[index + 1] = key

        else:
            # Busca el hijo donde debe insertarse la clave
            while index >= 0 and key < node.keys[index]:
                index -= 1

            index += 1

            maximum_keys = 2 * self.t - 1

            # Si el hijo está lleno, se divide antes de insertar
            if len(node.children[index].keys) == maximum_keys:
                self._split_child(node, index)

                if key > node.keys[index]:
                    index += 1

            self._insert_non_full(node.children[index], key)

    def _split_child(self, parent, child_index):
        """
        Divide un hijo lleno en dos nodos.

        La clave central sube al nodo padre.
        """

        t = self.t

        full_child = parent.children[child_index]
        new_child = BTreeNode(leaf=full_child.leaf)

        # La clave central que subirá al padre
        middle_key = full_child.keys[t - 1]

        # El nuevo nodo recibe las claves de la derecha
        new_child.keys = full_child.keys[t:]

        # El nodo original conserva las claves de la izquierda
        full_child.keys = full_child.keys[:t - 1]

        # Si no es hoja, también se dividen los hijos
        if not full_child.leaf:
            new_child.children = full_child.children[t:]
            full_child.children = full_child.children[:t]

        # Se inserta el nuevo hijo en el padre
        parent.children.insert(child_index + 1, new_child)

        # La clave central se inserta en el padre
        parent.keys.insert(child_index, middle_key)

    def traverse(self):
        """
        Retorna las claves ordenadas.
        """

        result = []
        self._traverse_recursive(self.root, result)
        return result

    def _traverse_recursive(self, node, result):
        for index, key in enumerate(node.keys):

            if not node.leaf:
                self._traverse_recursive(node.children[index], result)

            result.append(key)

        if not node.leaf:
            self._traverse_recursive(
                node.children[len(node.keys)],
                result
            )

    def print_tree(self):
        """
        Muestra el árbol nivel por nivel.
        """

        self._print_recursive(self.root, level=0)

    def _print_recursive(self, node, level):
        print(f"Nivel {level}: {node.keys}")

        if not node.leaf:
            for child in node.children:
                self._print_recursive(child, level + 1)


if __name__ == "__main__":
    tree = BTree(minimum_degree=2)

    values = [
        10, 20, 5, 6, 12,
        30, 7, 17, 3, 2,
        8, 15, 25
    ]

    for value in values:
        tree.insert(value)

    print("B-Tree:")
    tree.print_tree()

    print("\nRecorrido ordenado:")
    print(tree.traverse())

    value_to_search = 17
    result = tree.search(value_to_search)

    if result:
        node, position = result
        print(
            f"\nEl valor {value_to_search} fue encontrado "
            f"en el nodo {node.keys}, posición {position}."
        )
    else:
        print(f"\nEl valor {value_to_search} no existe.")