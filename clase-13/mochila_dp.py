def mochila_dinamica(
    pesos: list[int],
    valores: list[int],
    capacidad: int
) -> int:
    """
    Calcula el valor máximo que puede llevar la mochila
    usando programación dinámica con tabulación.

    :param pesos: Peso de cada objeto.
    :param valores: Valor de cada objeto.
    :param capacidad: Capacidad máxima de la mochila.
    :return: Valor máximo que puede obtenerse.
    """

    cantidad_objetos = len(pesos)

    # Crear una tabla llena de ceros.
    # Filas: objetos disponibles.
    # Columnas: capacidades de 0 hasta capacidad.
    tabla = [
        [0] * (capacidad + 1)
        for _ in range(cantidad_objetos + 1)
    ]

    # Empezamos en 1 porque la fila 0 representa
    # una mochila sin objetos disponibles
    for objeto in range(1, cantidad_objetos + 1):
        peso_actual = pesos[objeto - 1]
        valor_actual = valores[objeto - 1]

        for capacidad_actual in range(1, capacidad + 1):

            # El objeto no cabe
            if peso_actual > capacidad_actual:
                tabla[objeto][capacidad_actual] = (
                    tabla[objeto - 1][capacidad_actual]
                )

            else:
                # Opción 1: no incluir el objeto
                excluir = tabla[objeto - 1][capacidad_actual]

                # Opción 2: incluir el objeto
                incluir = valor_actual + tabla[
                    objeto - 1
                ][capacidad_actual - peso_actual]

                tabla[objeto][capacidad_actual] = max(
                    incluir,
                    excluir
                )

    return tabla[cantidad_objetos][capacidad]


pesos = [1, 3, 4, 5]
valores = [1, 4, 5, 7]
capacidad = 7

resultado = mochila_dinamica(
    pesos,
    valores,
    capacidad
)

print(f"Valor máximo: {resultado}")