class NodeTree:
    """
    Representa un nodo de un árbol binario.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        """
        Indica si el nodo es una hoja.
        """
        return self.left is None and self.right is None

    def __str__(self):
        return str(self.value)