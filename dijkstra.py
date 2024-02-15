import networkx as nx
import matplotlib.pyplot as plt
from priority_queue import PriorityQueue


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

    def visualize_step(self, curr_node):
        plt.clf()
        color_map = []
        for node in self.G.nodes:
            if node == self.src:
                color_map.append('yellow')
            elif self.visited[node]:
                color_map.append('blue')
            elif node in [n for _, n in self.pq.heap]:
                color_map.append('red')
            else:
                color_map.append('gray')

        if curr_node is not None and curr_node is not self.src:
            idx = list(self.G.nodes).index(curr_node)
            color_map[idx] = 'green'

        nx.draw(self.G, pos=self.pos, node_color=color_map, with_labels=True, edge_color='gray')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=nx.get_edge_attributes(self.G, 'weight'))

        legend_labels = {'Yellow': 'Source', 'Blue': 'Visited', 'Red': 'Priority Queue', 'Green': 'Current'}
        legend_patches = [plt.Line2D([0], [0], marker='o', color=color, label=label, linestyle='') for color, label in legend_labels.items()]
        plt.legend(handles=legend_patches, loc='best')

        plt.draw()
        plt.pause(0.75) 

    def dijkstra(self, visualize=False):
        self.pq.push((0, self.src))
        curr_node = self.src

        if visualize:
            plt.ion()

        while not self.pq.empty():
            curr_dist, curr_node = self.pq.pop()

            if visualize:
                self.visualize_step(curr_node)

            self.visited[curr_node] = True
            
            for neighbor in self.G.neighbors(curr_node):
                if not self.visited[neighbor]:
                    weight = self.G[curr_node][neighbor]['weight']
                    new_dist = curr_dist + weight
                    if new_dist < self.distances[neighbor]:
                        self.distances[neighbor] = new_dist
                        self.pred[neighbor] = curr_node
                        self.pq.push((self.distances[neighbor], neighbor))

            

            
        
        
        print(curr_node)
        if visualize:
            plt.ioff()  
            plt.show() 

    
    def recreate_path(self, target):
        path_colors = {node: 'grey' for node in self.G.nodes}
        path_colors[self.src] = 'yellow'
        path_colors[target] = 'green'  

        path = [target]
        p = self.pred[target]

        while p is not None:
            path.append(p)
            path_colors[p] = 'yellow'
            p = self.pred[p]

        edge_colors = ['grey' if path_colors[edge[0]] == 'grey' or path_colors[edge[1]] == 'grey' else 'yellow' for edge in self.G.edges()]
        nx.draw(self.G, pos=self.pos, node_color=[path_colors[node] for node in self.G.nodes],
                with_labels=True, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=nx.get_edge_attributes(self.G, 'weight'))
        plt.show()

        return path


