# Vértices del grafo
vertices = ["A", "B", "C", "D"]

# Matriz de adyacencia
# 1 = existe conexión
# 0 = no existe conexión

matriz = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

# Mostrar conexiones
for i in range(len(vertices)):
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            print(vertices[i], "está conectado con", vertices[j])