from collections import deque

from node_tree import NodeTree


def level_order(root):
    """
    Recorre un árbol por niveles (Breadth-First Search).

    Visita primero la raíz, luego todos los nodos del nivel 1,
    después los del nivel 2 y así sucesivamente.
    """

    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:

        current = queue.popleft()

        print(current.value, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


def create_example_tree():
    """
            10
          /    \
         5      15
       /  \    /  \
      3    7  12  20
     / \          /
    1   4        18
    """

    root = NodeTree(10)

    root.left = NodeTree(5)
    root.right = NodeTree(15)

    root.left.left = NodeTree(3)
    root.left.right = NodeTree(7)

    root.right.left = NodeTree(12)
    root.right.right = NodeTree(20)

    root.left.left.left = NodeTree(1)
    root.left.left.right = NodeTree(4)

    root.right.right.left = NodeTree(18)

    return root


if __name__ == "__main__":

    tree = create_example_tree()

    print("Recorrido por niveles:")
    level_order(tree)