# Dijkstra's Algorithm with Priority Queue

## Overview

This project implements Dijkstra's shortest path algorithm using a priority queue data structure for efficient node selection. It provides functionality to find the shortest path from a given source node to all other nodes in a weighted graph and offers visualization capabilities to understand the algorithm's execution.

## Priority Queue

The priority queue utilized in this project is implemented in the `priority_queue.py` file. It supports efficient insertion and extraction of items based on priority, achieved through a binary heap structure. The priority queue's operations, such as `_heapify_up` and `_heapify_down`, ensure that the heap property is maintained, enabling efficient priority-based operations with a time complexity of O(log n).

- **_heapify_up**: Moves an element up in the heap until the heap property is satisfied, ensuring that the element has higher priority than its parent.
- **_heapify_down**: Moves an element down in the heap until the heap property is satisfied, ensuring that the element has lower priority than its children.

## Dijkstra's Algorithm

Dijkstra's algorithm is a graph search algorithm used to find the shortest path from a source node to all other nodes in a weighted graph. It operates by iteratively selecting the node with the shortest distance from the source and updating the distances to its neighbors accordingly.

### Visualization

The project provides visualization capabilities using Matplotlib to illustrate the execution of Dijkstra's algorithm. Nodes are colored based on their state during the algorithm's execution:
- **Yellow**: Source node
- **Blue**: Visited node
- **Red**: Nodes in the priority queue
- **Green**: Current node being processed

Edges are colored to represent the shortest path found during the algorithm's execution.

