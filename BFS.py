import networkx as nx
import GUI

queue = []  # Initialize a queue
visited = []  # List for visited nodes.


def bfs(visited, graph, node):  # function for BFS
    our_visited = []
    visited.append(node)
    queue.append(node)
    visited_edges = []
    is_Goal = nx.get_node_attributes(GUI.G, "is_goal")
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        our_visited.append(m)
        goal = is_Goal[m]
        if goal:
            #Ziad_Edits
            visited.append(goal)
            print("Etba3 el Nodes")
            print(visited)
            print("Etba3 el Nodes")
            visited_edges.append(([m, goal]))
            print("Etba3 el Edges")
            print(visited_edges)
            print("Done")
            #Ziad_Edits
            return our_visited, visited_edges
        else:
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    visited_edges.append([m, neighbour])


def BFS_helper():
    graph = GUI.G.adj
    visited_nodes, visited_edges = bfs(visited, graph, list(graph.keys())[0])
    print(f"the visited nodes are: {visited_nodes}")
    print(f"the visited edges are: {visited_edges}")
    recurser_visualizer(visited_nodes, visited_edges)
    GUI.showTree(True)


def recurser_visualizer(visited_nodes, visited_edges, counter=0):
    max = visited_nodes[-1]
    if counter == len(visited_edges): return

    for j in range(len(visited_edges[counter]) - 1):
        if visited_edges[counter][j + 1] == max: return
        nx.set_edge_attributes(GUI.G, {(visited_edges[counter][j], visited_edges[counter][j + 1]): {"color": "b"}})
        print(visited_edges[counter][j], visited_edges[counter][j + 1])
        GUI.showTree(True)

    counter += 1
    recurser_visualizer(visited_nodes, visited_edges, counter)


def visualizer(visited_nodes, visited_edges):
    max = visited_nodes[-1]
    for i in range(len(visited_edges)):
        for j in range(len(visited_edges[i]) - 1):
            if visited_edges[i][j] == max:
                nx.set_edge_attributes(GUI.G, {(visited_edges[i][j], visited_edges[i][j + 1]): {"color": "b"}})
                GUI.showTree(True)
                nx.set_edge_attributes(GUI.G, {(visited_edges[i][j], visited_edges[i][j + 1]): {"color": "b"}})
                print(visited_edges[i][j], visited_edges[i][j + 1])
                return -1

# visited_nodes = ['A', 'B', 'C', 'E', 'H', 'D', 'F']
# visited edges = [['A', 'B'], ['A', 'C'], ['B', 'E'], ['B', 'H'], ['C', 'D'], ['E', 'F'], ['D', 'G']]
