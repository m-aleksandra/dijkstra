import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import Dijkstra

# Manually specified positions for 20 nodes
positions = {
    1: (0, 1),
    2: (1, 2),
    3: (2, 1),
    4: (1, 0),
    5: (-1, 2),
    6: (-2, 1),
    7: (-1, 0),
    8: (0, -1),
    9: (1, -2),
    10: (2, -1),
    11: (-1, -2),
    12: (-2, -1),
    13: (0.5, 1.5),
    14: (1.5, 0.5),
    15: (1.5, -0.5),
    16: (0.5, -1.5),
    17: (-0.5, 1.5),
    18: (-1.5, 0.5),
    19: (-1.5, -0.5),
    20: (-0.5, -1.5),
}

# Create a new weighted graph
G = nx.Graph()

# Add nodes with the specified positions
for node, pos in positions.items():
    G.add_node(node, pos=pos)

# Manually add edges with weights
edges_with_weights = [
    (1, 2, 1.5),
    (2, 3, 2.0),
  
    (16, 1, 3.0),
    (5, 6, 1.5),
    (6, 7, 2.0),
    (7, 20, 2.5),
    (1, 8, 25),
    (8, 17, 3.0),
    (9, 10, 1.5),
    (9, 11, 2.0),
    (17, 13, 8.0),
    (11, 12, 2.5),
    (12, 19, 3.0),
    (13, 14, 1.0),
    (14, 15, 7.0),
    (15, 16, 1.0),
    (16, 13, 1.0),
    (17, 18, 1.0),
    (18, 19, 6.0),
    (19, 20, 1.0),
    (20, 17, 1.0),
    (1, 13, 1.0),
    (2, 14, 1.0),
    (3, 15, 1.0),
    (4, 16, 1.0),
    (5, 17, 1.0),
    (6, 18, 1.0),
    (7, 19, 1.0),
    (8, 20, 1.0),
]


G.add_weighted_edges_from(edges_with_weights)

# Draw the graph
nx.draw(G, positions, with_labels=True, node_size=500, node_color='lightblue', font_size=10)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels)

# plt.title("Graph with Manually Specified Positions and Weights")
# plt.show()

D = Dijkstra(G, positions, 1)
D.dijkstra(True)
D.recreate_path(10)

print(D.pred)
