from collections import deque

import networkx as nx

import GUI


class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def breadth_first_search(self, start, goal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.appendleft(node); came_from[node] = current
            print(', '.join(fringe))
        if found: print(); return came_from
        else: print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' =>', goal, end='')


    def __str__(self):
        return str(self.edges)
G = nx.DiGraph()

G.add_node("A", weight=10, is_goal=False, node_color="yellow")
G.add_node("B", weight=9, is_goal=False, node_color="yellow")
G.add_node("C", weight=7, is_goal=False, node_color="yellow")
G.add_node("D", weight=8, is_goal=False, node_color="yellow")
G.add_node("E", weight=6, is_goal=False, node_color="yellow")
G.add_node("F", weight=3, is_goal=False, node_color="yellow")
G.add_node("G", weight=1, is_goal=False, node_color="yellow")
G.add_node("H", weight=0, is_goal=True, node_color="blue")
G.add_node("I", weight=2, is_goal=False, node_color="yellow")
G.add_node("J", weight=4, is_goal=False, node_color="yellow")
G.add_node("K", weight=6, is_goal=False, node_color="yellow")

G.add_edge("A", "B", weight=2, color='r')
G.add_edge("A", "I", weight=3, color='r')
G.add_edge("B", "C", weight=3, color='r')
G.add_edge("C", "D", weight=4, color='r')
G.add_edge("C", "F", weight=3, color='r')
G.add_edge("F", "G", weight=1, color='r')
G.add_edge("F", "H", weight=4, color='r')
G.add_edge("D", "E", weight=1, color='r')
G.add_edge("I", "H", weight=12, color='r')
G.add_edge("I", "J", weight=1, color='r')
G.add_edge("I", "K", weight=1, color='r')
# graph = Graph(directed=False)
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'S')
# graph.add_edge('S', 'G')
# graph.add_edge('S', 'C')
# graph.add_edge('C', 'F')
# graph.add_edge('G', 'F')
# graph.add_edge('C', 'D')
# graph.add_edge('C', 'E')
# graph.add_edge('E', 'H')
# graph.add_edge('G', 'H')
start, goal = 'A', 'H'
graph = G.adj
traced_path = graph.breadth_first_search(start, goal)
if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal);print()