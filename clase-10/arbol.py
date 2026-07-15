from node_tree import NodeTree
# Crear los nodos
raiz = NodeTree("Universidad")

facultad_ingenieria = NodeTree("Facultad de Ingeniería")
facultad_ciencias = NodeTree("Facultad de Ciencias")

informatica = NodeTree("Informática")
industrial = NodeTree("Ingeniería Industrial")
matematica = NodeTree("Matemática")
fisica = NodeTree("Física")

# Construir el árbol
raiz.agregar_hijo(facultad_ingenieria)
raiz.agregar_hijo(facultad_ciencias)

facultad_ingenieria.agregar_hijo(informatica)
facultad_ingenieria.agregar_hijo(industrial)

facultad_ciencias.agregar_hijo(matematica)
facultad_ciencias.agregar_hijo(fisica)

# Mostrar el árbol
raiz.mostrar()