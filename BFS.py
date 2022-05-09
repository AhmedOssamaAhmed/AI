import networkx as nx

import GUI
import time
queue = []  # Initialize a queue
visited = []  # List for visited nodes.


def bfs(visited, graph, node):  # function for BFS
    our_visited=[]
    visited.append(node)
    queue.append(node)

    is_Goal = nx.get_node_attributes(GUI.G,"is_goal")
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        our_visited.append(m)
        goal = is_Goal[m]
        if goal :
            return our_visited
        else:
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

def BFS_helper():
    graph = GUI.G.adj
    visited_nodes = bfs(visited, graph, list(graph.keys())[0])
    print(f"the visited nodes are: {visited_nodes}")
    visualizer(visited_nodes)
    # GUI.showTree(True)

def visualizer(visited_nodes):
    for i in range(len(visited_nodes)-1):
        nx.set_edge_attributes(GUI.G, {(visited_nodes[i], visited_nodes[i+1]): {"color": "b"}})
        GUI.showTree(True)
        time.sleep(10)
