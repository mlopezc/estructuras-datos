def mochila_recursiva(
    pesos: list[int],
    valores: list[int],
    capacidad: int,
    cantidad_objetos: int
) -> int:
    """
    Calcula el valor máximo que puede llevar la mochila
    usando recursividad pura.

    :param pesos: Peso de cada objeto.
    :param valores: Valor de cada objeto.
    :param capacidad: Capacidad máxima de la mochila.
    :param cantidad_objetos: Cantidad de objetos disponibles.
    :return: Valor máximo que puede obtenerse.
    """

    # Caso base: no quedan objetos o no queda capacidad
    if cantidad_objetos == 0 or capacidad == 0:
        return 0

    indice = cantidad_objetos - 1

    # Si el objeto actual pesa más que la capacidad,
    # no puede incluirse
    if pesos[indice] > capacidad:
        return mochila_recursiva(
            pesos,
            valores,
            capacidad,
            cantidad_objetos - 1
        )

    # Opción 1: incluir el objeto actual
    incluir = valores[indice] + mochila_recursiva(
        pesos,
        valores,
        capacidad - pesos[indice],
        cantidad_objetos - 1
    )

    # Opción 2: no incluir el objeto actual
    excluir = mochila_recursiva(
        pesos,
        valores,
        capacidad,
        cantidad_objetos - 1
    )

    return max(incluir, excluir)


pesos = [1, 3, 4, 5]
valores = [1, 4, 5, 7]
capacidad = 7

resultado = mochila_recursiva(
    pesos,
    valores,
    capacidad,
    len(pesos)
)

print(f"Valor máximo: {resultado}")