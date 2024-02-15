from dijkstra import Dijkstra
from graph_examples import big_graph, positions_big

D = Dijkstra(big_graph, positions_big, 1)
D.dijkstra(True)
D.recreate_path(10)