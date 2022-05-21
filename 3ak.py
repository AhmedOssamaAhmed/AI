import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
G = nx.DiGraph()


def toUndirected():
    temp_graph = G.copy()
    weight = nx.get_edge_attributes(G, 'weight')
    edges = list(G.edges())
    print(edges)
    print(weight)
    print(list(weight.values())[0])
    print(edges[0])
    for i in range(len(edges)):
        G.add_edge(edges[i][1], edges[i][0], weight=list(weight.values())[i], color='r')
    return temp_graph


def toDirected(temp_graph,G):
    G.clear()
    G = temp_graph
    return G

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

temp = toUndirected()
G = toDirected(temp,G)

node_we = nx.get_node_attributes(G, 'weight')
labels = nx.get_edge_attributes(G, 'weight')
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
# plt.show()
# first_dict = G.adj
#
# major_key = list(first_dict.items())[0][0]
# value = list(first_dict.items())[0][1]
# minor_key = list(value.items())[0][0]
# minor_value_helper = list(value.items())[0][1]
# minor_value = list(minor_value_helper.items())[0][1]
# print(major_key)
# print(minor_key)
# print(minor_value)
node_weights = nx.get_node_attributes(G, 'weight')

# plt.show()


def find_goal(G):
    is_Goal = nx.get_node_attributes(G, "is_goal")
    for node in is_Goal.items():
        if node[1] is True:
            # print(node[0])
            return node[0]


def graphMap(graph):
    first_dict = graph.adj
    graph_len = len(list(first_dict.items()))
    our_dict = {}
    # looping on the whole graph
    for j in range(graph_len):
        major_key = list(first_dict.items())[j][0]
        value = list(first_dict.items())[j][1]
        # second loop making tuples
        major_list = []
        for i in range(len(value)):
            minor_key = list(value.items())[i][0]
            minor_value_helper = list(value.items())[i][1]
            minor_value = list(minor_value_helper.items())[0][1]
            arr = []
            arr.append(minor_key)
            arr.append(minor_value)
            arr = tuple(arr)
            major_list.append(arr)
            # print(major_list)
        our_dict.update({major_key: major_list})
        # print(our_dict)
    return our_dict


def toUndirected():
    weight = nx.get_edge_attributes(G, 'weight')
    edges = list(G.edges())
    print(edges)
    print(weight)
    print(list(weight.values())[0])
    print(edges[0])
    for i in range(len(edges)):
        G.add_edge(edges[i][1], edges[i][0], weight=list(weight.values())[i], color='r')


def toDirected():
    edges = list(G.edges())
    for i in range(len(edges)):
        G.remove_edge(edges[i][1], edges[i][0])

# print(find_goal(G))
# print(graphMap(G))

# print(list(value.items())[0][0])

print(f"nnnnnnnnnnnnnn{G.edges}")