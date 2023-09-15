def dijkstra(Grafo, salida):
    # Inicialización de variables
    dist, prev = {}, {}
    result = []
    
    # Asignación de valores iniciales
    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0
    
    
  # Creación de lista ElementosVertices con todos los vértices del grafo
    ElementosVertices = [vertice for vertice in Grafo]

    while ElementosVertices:
        # Selecciona el vértice con la menor distancia
        u = min(ElementosVertices, key=dist.get)
        ElementosVertices.remove(u)
        result.append(u)

        # Actualiza las distancias de los vecinos del vértice seleccionado
        for vecino in Grafo[u]:
            if vecino in ElementosVertices and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev

def ruta_mas_corta(prev, dist, inicio, fin):
    # Inicialización de variables   
    ruta = [fin]
    distancias = [dist[fin]]
    # Bucle para encontrar la ruta más corta
    while ruta[-1] != inicio:
        ruta.append(prev[ruta[-1]])
        distancias.append(dist[ruta[-1]])
        
    # Invierte las listas para que estén en el orden correcto
    ruta.reverse()
    distancias.reverse()
    return ruta, distancias


#Representacion de las cuidades como nodos con sus respectivos pesos
grafo = {
    'Ellensburg': {'Pendleton': 168, 'Spokane': 175},
    'Pendleton': {'Spokane': 200, 'Missoula': 356, 'Ellensburg': 168},
    'Spokane': {'Bonners Ferry': 112, 'Missoula': 199, 'Ellensburg': 175, 'Pendleton': 200},
    'Bonners Ferry': {'West Glacier': 176, 'Missoula': 249, 'Spokane': 112},
    'West Glacier': {'Missoula': 151, 'Bonners Ferry': 176, 'Helena': 243, 'Great Falls': 211, 'Havre': 231},
    'Missoula': {'West Glacier': 151, 'Bonners Ferry': 249, 'Spokane': 199, 'Pendleton': 356, 'Helena': 111, 'Butte': 119},
    'Butte': {'Missoula': 119, 'Helena': 65},
    'Helena': {'Butte': 65, 'Missoula': 111, 'West Glacier': 243, 'Great Falls': 91},
    'Great Falls': {'Helena': 91, 'West Glacier': 211, 'Havre': 115},
    'Havre': {'Great Falls': 115, 'West Glacier': 231},
}


# Imprime la información de la ruta y los nodos explorados
def imprimir_ruta_y_exploracion(grafo, ruta, distancias_ruta):
    for i in range(1, len(ruta)+1):
        print("Frontera={} (peso = {} km); Explored={}".format(ruta[i-1], distancias_ruta[i-1], ', '.join(grafo[ruta[i-1]].keys())))

inicio = 'Ellensburg'
destino = 'Havre'
s, distancia, previos = dijkstra(grafo, inicio)
ruta, distancias_ruta = ruta_mas_corta(previos, distancia, inicio, destino)

print(f"La ruta desde {inicio} hasta {destino} es:")
imprimir_ruta_y_exploracion(grafo, ruta, distancias_ruta)
for i in range(len(ruta)):
    if i == len(ruta) - 1:
        print(f"{ruta[i]}")
    else:
        print(f"{ruta[i]} ({distancias_ruta[i+1] - distancias_ruta[i]} km) -> ", end="")
print(f"con una distancia total de {distancia[destino]} km.")

