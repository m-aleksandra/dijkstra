import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
from priority_queue import PriorityQueue
from typing import List, Union

class Dijkstra:
    def __init__(self, G, pos, src):
        self.G = G
        self.pos = pos
        self.src = src
        self.pq = PriorityQueue()
        self.pred = {node: None for node in G.nodes}
        self.visited = {node: False for node in G.nodes}
        self.distances = {node: float('infinity') for node in G.nodes}
        self.distances[src] = 0
        self.current_node = None  # For visualization

    def _dijkstra_step(self) -> bool:
        if self.pq.empty():
            return False  

        curr_dist, curr_node = self.pq.pop()

        if self.visited[curr_node]:
            return True 

        self.current_node = curr_node
        self.visited[curr_node] = True

        for neighbor in self.G.neighbors(curr_node):
            if not self.visited[neighbor]:
                weight = self.G[curr_node][neighbor]['weight']
                new_dist = curr_dist + weight
                if new_dist < self.distances[neighbor]:
                    self.distances[neighbor] = new_dist
                    self.pred[neighbor] = curr_node
                    self.pq.push((new_dist, neighbor))
        return True

    def _animate(self, i) -> None:

        plt.cla()
        color_map = []
        for node in self.G.nodes:
            if node == self.src:
                color_map.append('yellow')
            elif node == self.current_node:
                color_map.append('green')
            elif self.visited[node]:
                color_map.append('blue')
            elif node in [n for _, n in self.pq.heap]:
                color_map.append('red')
            else:
                color_map.append('gray')

        nx.draw(self.G, pos=self.pos, node_color=color_map, with_labels=True,
                edge_color='grey', node_size=500)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels)

        plt.text(1.05, 1.0, 'Legend:', transform=plt.gca().transAxes, verticalalignment='top')
        plt.text(1.05, 0.95, 'Yellow = Source', transform=plt.gca().transAxes, verticalalignment='top', color='yellow')
        plt.text(1.05, 0.90, 'Green = Current', transform=plt.gca().transAxes, verticalalignment='top', color='green')
        plt.text(1.05, 0.85, 'Blue = Visited', transform=plt.gca().transAxes, verticalalignment='top', color='blue')
        plt.text(1.05, 0.80, 'Red = In Priority Queue', transform=plt.gca().transAxes, verticalalignment='top', color='red')

        plt.subplots_adjust(right=0.7)

        if not self._dijkstra_step():
            plt.cla()
            color_map = ['blue' for _ in self.G.nodes()]
            nx.draw(self.G, pos=self.pos, node_color=color_map, with_labels=True,
                edge_color='grey', node_size=500)
            nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels)
            plt.text(1.05, 1.0, 'DONE', transform=plt.gca().transAxes, verticalalignment='top')
            return  


    def dijkstra(self, visualise=True) -> Union[float, int]:
        self.pq.push((0, self.src))

        if visualise:
            anim = FuncAnimation(plt.gcf(), self._animate, interval=750, save_count=0)
            plt.show()
        else:
            while self._dijkstra_step(): pass
        
        return self.distances
    
    def recreate_path(self, target, visualise=True) -> List[int]:
        if visualise:
            path_colors = {node: 'grey' for node in self.G.nodes}
            path_colors[self.src] = 'yellow'
            path_colors[target] = 'green'

        path = [target]
        while target is not None:
            target = self.pred[target]
            if target is not None:
                path.append(target)
        path = path[::-1]  


        if visualise:
            edge_colors = []
            for edge in self.G.edges():
                if edge[0] in path and edge[1] in path:
                    if abs(path.index(edge[0]) - path.index(edge[1])) == 1:
                        edge_colors.append('orange')
                    else:
                        edge_colors.append('grey')
                else:
                    edge_colors.append('grey')

            nx.draw(self.G, pos=self.pos, node_color=[path_colors[node] for node in self.G.nodes],
                    with_labels=True, edge_color=edge_colors, node_size=500)
            edge_labels = nx.get_edge_attributes(self.G, 'weight')
            nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels)
            plt.show()

        return path
