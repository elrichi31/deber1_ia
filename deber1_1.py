
import networkx as nx
import matplotlib.pyplot as plt

# Creación del grafo
G = nx.Graph()

# Nodos
nodos = ["A", "C", "D", "B"]
G.add_nodes_from(nodos)

# Aristas con sus pesos
aristas = [("A", "C", 50), ("A", "D", 80), ("C", "B", 70), ("D", "B", 50)]
G.add_weighted_edges_from(aristas)

# Dibuja el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, width=2, edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Representación del Grafo")
plt.show()
