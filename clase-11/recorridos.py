from node_tree import NodeTree


def pre_order(node):
    """
    Recorrido preorden:
    raíz -> izquierda -> derecha
    """
    if node is None:
        return

    print(node.value, end=" ")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    """
    Recorrido inorden:
    izquierda -> raíz -> derecha
    """
    if node is None:
        return

    in_order(node.left)
    print(node.value, end=" ")
    in_order(node.right)


def post_order(node):
    """
    Recorrido postorden:
    izquierda -> derecha -> raíz
    """
    if node is None:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.value, end=" ")


def create_example_tree():
    """
    Crea el siguiente árbol:

              10
             /  \
            5    15
           / \   / \
          3   7 12  20
    """

    root = NodeTree(10)

    root.left = NodeTree(5)
    root.right = NodeTree(15)

    root.left.left = NodeTree(3)
    root.left.right = NodeTree(7)

    root.right.left = NodeTree(12)
    root.right.right = NodeTree(20)

    return root


if __name__ == "__main__":
    tree = create_example_tree()

    print("Recorrido preorden:")
    pre_order(tree)

    print("\n\nRecorrido inorden:")
    in_order(tree)

    print("\n\nRecorrido postorden:")
    post_order(tree)