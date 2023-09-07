def dijkstra(Grafo, salida, llegada):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev

def ruta_mas_corta(prev, inicio, fin):
    ruta = [fin]
    while ruta[-1] != inicio:
        ruta.append(prev[ruta[-1]])
    ruta.reverse()
    return ruta

grafo = {
    'a': {'b': 4, 'c': 3},
    'b': {'d': 5},
    'c': {'b': 2, 'd': 3, 'e': 6},
    'd': {'f': 5, 'e': 1},
    'e': {'g': 5},
    'g': {'z': 4},
    'f': {'g': 2, 'z': 7},
    'z': {}
}

inicio = 'a'
destino = 'z'
s, distancia, previos = dijkstra(grafo, inicio, destino)
ruta = ruta_mas_corta(previos, inicio, destino)
print(f"La ruta más corta desde {inicio} hasta {destino} es: {' -> '.join(ruta)} con una distancia de {distancia[destino]}")
