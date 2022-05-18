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

print(find_goal(G))
# print(graphMap(G))

# print(list(value.items())[0][0])
