import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.DiGraph()
G.add_node("A", weight=15121, is_goal=False)
G.add_node("B", weight=15151, is_goal=False)
G.add_node("C", weight=154, is_goal=False)
G.add_node("D", weight=155, is_goal=False)
G.add_node("E", weight=115, is_goal=False)
G.add_node("F", weight=1, is_goal=False)
G.add_node("G", weight=10, is_goal=True)

G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "D", weight=6)
G.add_edge("B", "E", weight=4)
G.add_edge("C", "F", weight=9)
G.add_edge("C", "G", weight=7)
node_we = nx.get_node_attributes(G, 'weight')
labels = nx.get_edge_attributes(G, 'weight')
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# print(node_we)
# plt.show()
#
# def get_path(G,goal_node):
#     path = []
#     starting_node = list(G.adj.keys())[0]
#     path.append(goal_node)
#     while "A" not in path :
#         for nodes in G.predecessors(path[-1]):
#             path.append(nodes)
#     print(path)
#     print(list(reversed(path)))
# get_path(G,"G")

# node= G.predecessors("G")
#
# for i in range(len(G)):
#     for nodes in node:
#         print(nodes)
#         node = G.predecessors(nodes)


queue = []  # Initialize a queue
visited = []  # List for visited nodes.

our_visited = []
visited_edges = []
def dfs(visited, graph, node):  # function for dfs


    if node not in visited:
        is_Goal = nx.get_node_attributes(G, "is_goal")
        goal = is_Goal[node]
        print(goal)
        if goal:
            print("reached goal node")
            print(f"visited {our_visited}")
            print(f"visited edges:{visited_edges}")
            return our_visited, visited_edges

        # print(node)
        visited.append(node)
        our_visited.append(node)
        for neighbour in graph[node]:
            print("reached iterations")
            neighbour = dfs(visited, graph, neighbour)
            visited_edges.append([node, neighbour])


graph = G.adj
x, y = dfs(visited, graph, "A")
print(f"our visited : {x}")
print(f"visited edges : {y}")
