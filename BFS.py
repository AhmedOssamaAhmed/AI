import networkx as nx
import os
import GUI
import time
queue = []  # Initialize a queue
visited = []  # List for visited nodes.


def bfs(visited, graph, node):  # function for BFS
    our_visited=[]
    visited.append(node)
    queue.append(node)
    visited_edges =[]
    is_Goal = nx.get_node_attributes(GUI.G,"is_goal")
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        our_visited.append(m)
        goal = is_Goal[m]
        if goal :
            return our_visited,visited_edges
        else:
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    visited_edges.append([m,neighbour])
def BFS_helper():
    graph = GUI.G.adj
    visited_nodes,visited_edges = bfs(visited, graph, list(graph.keys())[0])
    print(f"the visited nodes are: {visited_nodes}")
    print(f"the visited edges are: {visited_edges}")
    visualizer(visited_nodes,visited_edges)
    GUI.showTree(True)

def visualizer(visited_nodes,visited_edges):

    max = visited_nodes[-1]
    for i in range(len(visited_edges)):
        for j in range(len(visited_edges[i])-1):
            nx.set_edge_attributes(GUI.G,{(visited_edges[i][j], visited_edges[i][j+1]): {"color": "b"}})
            print(visited_edges[i][j],visited_edges[i][j+1])
            # GUI.showTree(True)

        if visited_edges[i][j+1] == max:
            return


#visited_nodes = ['A', 'B', 'C', 'E', 'H', 'D', 'F']
#visited edges = [['A', 'B'], ['A', 'C'], ['B', 'E'], ['B', 'H'], ['C', 'D'], ['E', 'F'], ['D', 'G']]