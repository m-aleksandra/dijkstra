from dijkstra import Dijkstra
from graph_examples import big_graph, positions_big, small_graph, positions_small


dijkstra_vis = Dijkstra(big_graph, positions_big, 1)
print(dijkstra_vis.dijkstra())
print(dijkstra_vis.recreate_path(15))
print(dijkstra_vis.recreate_path(16))
print(dijkstra_vis.recreate_path(10))
print(dijkstra_vis.recreate_path(18))
