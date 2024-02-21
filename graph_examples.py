import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import Dijkstra

# Manually specified positions for 20 nodes
positions_big = {
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

big_graph = nx.Graph()

for node, pos in positions_big.items():
    big_graph.add_node(node, pos=pos)

edges_with_weights_b = [
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


big_graph.add_weighted_edges_from(edges_with_weights_b)

positions_small = {
    1: (0, 0),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (0.5, 2),
}

edges_with_weights_s = {
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 6),
    (1, 4, 1),
    (1, 3, 2),
    (2, 5, 5),
    (3, 5, 5),
}

small_graph = nx.Graph()

for node, pos in positions_small.items():
    small_graph.add_node(node, pos=pos)

small_graph.add_weighted_edges_from(edges_with_weights_s)
