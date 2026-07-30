from bisect import bisect_left, bisect_right


class BPlusTreeNode:
    """
    Nodo de un B+ Tree.

    Los nodos hoja almacenan claves y valores.
    Los nodos internos almacenan claves y referencias a hijos.
    """

    def __init__(self, leaf=False):
        self.leaf = leaf

        self.keys = []
        self.children = []

        # Solo se utiliza en nodos hoja
        self.values = []

        # Enlace hacia la siguiente hoja
        self.next = None


class BPlusTree:
    """
    Implementación educativa de un B+ Tree.

    order representa la cantidad máxima de hijos
    que puede tener un nodo interno.

    La cantidad máxima de claves es:
        order - 1
    """

    def __init__(self, order=4):
        if order < 3:
            raise ValueError("El orden debe ser al menos 3.")

        self.order = order
        self.root = BPlusTreeNode(leaf=True)

    def search(self, key):
        """
        Busca una clave y retorna su valor.

        Si no existe, retorna None.
        """

        leaf = self._find_leaf(key)

        position = bisect_left(leaf.keys, key)

        if (
            position < len(leaf.keys)
            and leaf.keys[position] == key
        ):
            return leaf.values[position]

        return None

    def _find_leaf(self, key):
        """
        Encuentra la hoja donde debería estar una clave.
        """

        current = self.root

        while not current.leaf:
            child_index = bisect_right(
                current.keys,
                key
            )

            current = current.children[child_index]

        return current

    def insert(self, key, value):
        """
        Inserta una clave y un valor.
        """

        root = self.root

        promoted = self._insert_recursive(
            root,
            key,
            value
        )

        # Si la raíz se dividió, se crea una nueva raíz
        if promoted is not None:
            promoted_key, new_right_node = promoted

            new_root = BPlusTreeNode(leaf=False)

            new_root.keys = [promoted_key]
            new_root.children = [
                root,
                new_right_node
            ]

            self.root = new_root

    def _insert_recursive(self, node, key, value):
        """
        Inserta recursivamente.

        Si el nodo se divide, retorna:
            (clave_promovida, nuevo_nodo_derecho)

        Si no se divide, retorna None.
        """

        if node.leaf:
            return self._insert_into_leaf(
                node,
                key,
                value
            )

        child_index = bisect_right(
            node.keys,
            key
        )

        promoted = self._insert_recursive(
            node.children[child_index],
            key,
            value
        )

        if promoted is None:
            return None

        promoted_key, new_right_child = promoted

        node.keys.insert(
            child_index,
            promoted_key
        )

        node.children.insert(
            child_index + 1,
            new_right_child
        )

        if len(node.keys) >= self.order:
            return self._split_internal(node)

        return None

    def _insert_into_leaf(self, leaf, key, value):
        """
        Inserta una clave dentro de una hoja.
        """

        position = bisect_left(
            leaf.keys,
            key
        )

        # Si la clave ya existe, actualiza su valor
        if (
            position < len(leaf.keys)
            and leaf.keys[position] == key
        ):
            leaf.values[position] = value
            return None

        leaf.keys.insert(position, key)
        leaf.values.insert(position, value)

        # Se divide si excede la capacidad
        if len(leaf.keys) >= self.order:
            return self._split_leaf(leaf)

        return None

    def _split_leaf(self, leaf):
        """
        Divide un nodo hoja.
        """

        middle = len(leaf.keys) // 2

        new_leaf = BPlusTreeNode(leaf=True)

        new_leaf.keys = leaf.keys[middle:]
        new_leaf.values = leaf.values[middle:]

        leaf.keys = leaf.keys[:middle]
        leaf.values = leaf.values[:middle]

        # Mantiene la lista enlazada de hojas
        new_leaf.next = leaf.next
        leaf.next = new_leaf

        # La primera clave de la nueva hoja sube al padre
        promoted_key = new_leaf.keys[0]

        return promoted_key, new_leaf

    def _split_internal(self, node):
        """
        Divide un nodo interno.
        """

        middle = len(node.keys) // 2

        promoted_key = node.keys[middle]

        new_internal = BPlusTreeNode(leaf=False)

        new_internal.keys = node.keys[middle + 1:]
        new_internal.children = node.children[middle + 1:]

        node.keys = node.keys[:middle]
        node.children = node.children[:middle + 1]

        return promoted_key, new_internal

    def range_search(self, start_key, end_key):
        """
        Retorna todos los registros cuyas claves estén
        dentro del rango indicado.
        """

        if start_key > end_key:
            raise ValueError(
                "La clave inicial no puede ser mayor "
                "que la clave final."
            )

        result = []

        current_leaf = self._find_leaf(start_key)

        while current_leaf is not None:

            for key, value in zip(
                current_leaf.keys,
                current_leaf.values
            ):
                if key > end_key:
                    return result

                if start_key <= key <= end_key:
                    result.append((key, value))

            current_leaf = current_leaf.next

        return result

    def get_all(self):
        """
        Retorna todos los registros ordenados.
        """

        result = []

        current = self.root

        # Baja hasta la hoja más a la izquierda
        while not current.leaf:
            current = current.children[0]

        # Recorre las hojas mediante los enlaces
        while current is not None:
            result.extend(
                zip(current.keys, current.values)
            )

            current = current.next

        return result

    def print_tree(self):
        """
        Muestra el árbol nivel por nivel.
        """

        queue = [(self.root, 0)]
        current_level = 0

        print(f"Nivel {current_level}: ", end="")

        while queue:
            node, level = queue.pop(0)

            if level != current_level:
                current_level = level
                print()
                print(
                    f"Nivel {current_level}: ",
                    end=""
                )

            if node.leaf:
                print(
                    f"Hoja{node.keys} ",
                    end=""
                )
            else:
                print(
                    f"Interno{node.keys} ",
                    end=""
                )

                for child in node.children:
                    queue.append(
                        (child, level + 1)
                    )

        print()

    def print_leaves(self):
        """
        Muestra la lista enlazada de hojas.
        """

        current = self.root

        while not current.leaf:
            current = current.children[0]

        while current is not None:
            print(current.keys, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()


if __name__ == "__main__":
    tree = BPlusTree(order=4)

    records = [
        (10, "Registro 10"),
        (20, "Registro 20"),
        (5, "Registro 5"),
        (6, "Registro 6"),
        (12, "Registro 12"),
        (30, "Registro 30"),
        (7, "Registro 7"),
        (17, "Registro 17"),
        (25, "Registro 25"),
        (3, "Registro 3"),
        (15, "Registro 15"),
        (27, "Registro 27")
    ]

    for key, value in records:
        tree.insert(key, value)

    print("B+ Tree:")
    tree.print_tree()

    print("\nHojas enlazadas:")
    tree.print_leaves()

    print("\nTodos los registros:")
    for key, value in tree.get_all():
        print(key, "->", value)

    value_to_search = 17

    print(
        f"\nBúsqueda de {value_to_search}:",
        tree.search(value_to_search)
    )

    print("\nBúsqueda por rango de 7 a 25:")

    for key, value in tree.range_search(7, 25):
        print(key, "->", value)