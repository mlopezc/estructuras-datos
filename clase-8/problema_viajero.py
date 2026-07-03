from itertools import permutations

def calcular_distancia(ruta, distancias):
    total = 0

    for i in range(len(ruta) - 1):
        ciudad_actual = ruta[i]
        ciudad_siguiente = ruta[i + 1]
        total += distancias[ciudad_actual][ciudad_siguiente]

    # Regresar a la ciudad inicial
    total += distancias[ruta[-1]][ruta[0]]

    return total


def problema_viajero(distancias, ciudad_inicio):
    ciudades = list(distancias.keys())

    # Quitamos la ciudad inicial porque siempre empezamos ahí
    ciudades.remove(ciudad_inicio)

    mejor_ruta = None
    menor_distancia = float("inf")

    # Probamos todos los posibles órdenes de visita
    for permutacion in permutations(ciudades):
        ruta = [ciudad_inicio] + list(permutacion)

        distancia_total = calcular_distancia(ruta, distancias)

        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            mejor_ruta = ruta

    # Agregamos el regreso al inicio
    mejor_ruta.append(ciudad_inicio)

    return mejor_ruta, menor_distancia


distancias = {
    "San José": {
        "Heredia": 10,
        "Alajuela": 20,
        "Cartago": 25
    },
    "Heredia": {
        "San José": 10,
        "Alajuela": 15,
        "Cartago": 30
    },
    "Alajuela": {
        "San José": 20,
        "Heredia": 15,
        "Cartago": 35
    },
    "Cartago": {
        "San José": 25,
        "Heredia": 30,
        "Alajuela": 35
    }
}

ruta, distancia = problema_viajero(distancias, "San José")

print("Mejor ruta:")
print(" -> ".join(ruta))

print("Distancia total:", distancia)