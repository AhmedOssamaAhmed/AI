import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.DiGraph()
G.add_node("A", weight=15121, is_goal=False)
G.add_node("B", weight=15151, is_goal=False)
G.add_node("C", weight=154, is_goal=False)
G.add_node("D", weight=155, is_goal=False)
G.add_node("E", weight=115, is_goal=False)
G.add_node("F", weight=1, is_goal=False)
G.add_node("G", weight=10, is_goal=True)

G.add_edge("A", "B", weight=1, color="r")
G.add_edge("A", "C", weight=2, color="b")
G.add_edge("B", "D", weight=6, color="g")
G.add_edge("B", "E", weight=4, color="g")
G.add_edge("C", "F", weight=9, color="r")
G.add_edge("C", "G", weight=7, color="b")
# colors = (nx.get_edge_attributes(G, 'color'))
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
print(f"this is the colors {colors}")
node_we = nx.get_node_attributes(G, 'weight')
labels = nx.get_edge_attributes(G, 'weight')
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True, edge_color=colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# nx.draw_networkx_edges(G,pos,edge_color=colors)
plt.show()
