class TrieNode:
    """
    Representa un nodo dentro de un Trie.

    Cada nodo almacena:
    - Un diccionario con sus hijos.
    - Un indicador que señala si termina una palabra.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Implementación de una estructura Trie.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserta una palabra en el Trie.
        """

        if not isinstance(word, str):
            raise TypeError("La palabra debe ser una cadena de texto.")

        if not word:
            raise ValueError("La palabra no puede estar vacía.")

        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.is_end_of_word = True

    def search(self, word):
        """
        Busca una palabra completa dentro del Trie.

        Retorna True si la palabra existe.
        Retorna False si no existe.
        """

        node = self._find_node(word)

        return (
            node is not None
            and node.is_end_of_word
        )

    def starts_with(self, prefix):
        """
        Indica si existe al menos una palabra
        que comience con el prefijo indicado.
        """

        return self._find_node(prefix) is not None

    def _find_node(self, text):
        """
        Busca el nodo correspondiente al último carácter
        de una palabra o prefijo.
        """

        if not isinstance(text, str):
            raise TypeError("El texto debe ser una cadena.")

        current = self.root

        for character in text:
            if character not in current.children:
                return None

            current = current.children[character]

        return current

    def autocomplete(self, prefix):
        """
        Retorna todas las palabras que comienzan
        con el prefijo indicado.
        """

        prefix_node = self._find_node(prefix)

        if prefix_node is None:
            return []

        words = []

        self._collect_words(
            prefix_node,
            prefix,
            words
        )

        return words

    def _collect_words(self, node, current_word, words):
        """
        Recorre recursivamente el Trie para recolectar palabras.
        """

        if node.is_end_of_word:
            words.append(current_word)

        for character, child in sorted(node.children.items()):
            self._collect_words(
                child,
                current_word + character,
                words
            )

    def get_all_words(self):
        """
        Retorna todas las palabras almacenadas en el Trie.
        """

        words = []

        self._collect_words(
            self.root,
            "",
            words
        )

        return words

    def delete(self, word):
        """
        Elimina una palabra del Trie.

        Retorna True si la palabra fue eliminada.
        Retorna False si la palabra no existía.
        """

        if not self.search(word):
            return False

        self._delete_recursive(
            self.root,
            word,
            index=0
        )

        return True

    def _delete_recursive(self, node, word, index):
        """
        Elimina recursivamente los nodos que ya no son necesarios.

        Retorna True cuando el nodo actual puede eliminarse.
        """

        # Se llegó al final de la palabra
        if index == len(word):
            node.is_end_of_word = False

            return len(node.children) == 0

        character = word[index]
        child = node.children[character]

        should_delete_child = self._delete_recursive(
            child,
            word,
            index + 1
        )

        if should_delete_child:
            del node.children[character]

        return (
            len(node.children) == 0
            and not node.is_end_of_word
        )

    def count_words(self):
        """
        Retorna la cantidad de palabras almacenadas.
        """

        return self._count_words_recursive(self.root)

    def _count_words_recursive(self, node):
        count = 1 if node.is_end_of_word else 0

        for child in node.children.values():
            count += self._count_words_recursive(child)

        return count

    def print_trie(self):
        """
        Muestra visualmente los caracteres del Trie.
        """

        print("Raíz")

        characters = sorted(self.root.children.items())

        for index, (character, child) in enumerate(characters):
            is_last = index == len(characters) - 1

            self._print_recursive(
                child,
                character,
                "",
                is_last
            )

    def _print_recursive(
        self,
        node,
        character,
        indentation,
        is_last
    ):
        connector = "└── " if is_last else "├── "
        end_marker = " *" if node.is_end_of_word else ""

        print(
            indentation
            + connector
            + character
            + end_marker
        )

        next_indentation = (
            indentation
            + ("    " if is_last else "│   ")
        )

        children = sorted(node.children.items())

        for index, (child_character, child_node) in enumerate(children):
            child_is_last = index == len(children) - 1

            self._print_recursive(
                child_node,
                child_character,
                next_indentation,
                child_is_last
            )


if __name__ == "__main__":
    trie = Trie()

    words = [
        "casa",
        "casado",
        "casamiento",
        "casco",
        "carro",
        "carta",
        "perro",
        "persona",
        "pescado"
    ]

    for word in words:
        trie.insert(word)

    print("Palabras almacenadas:")
    print(trie.get_all_words())

    print("\nCantidad de palabras:")
    print(trie.count_words())

    print("\nBuscar 'casa':")
    print(trie.search("casa"))

    print("\nBuscar 'cas':")
    print(trie.search("cas"))

    print("\n¿Existe el prefijo 'cas'?")
    print(trie.starts_with("cas"))

    print("\nAutocompletado para 'cas':")
    print(trie.autocomplete("cas"))

    print("\nAutocompletado para 'per':")
    print(trie.autocomplete("per"))

    print("\nEstructura del Trie:")
    trie.print_trie()

    print("\nEliminando 'casado':")
    trie.delete("casado")

    print(trie.get_all_words())