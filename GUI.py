import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

isGoal = False


def switch():
    global isGoal
    if isGoal:
        is_goal_button.config(image=off)
        isGoal = False
    else:

        is_goal_button.config(image=on)
        isGoal = True
    print(isGoal)


def getNodeData():
    nodeName = node_name.get("1.0", "end-1c")
    nodeWeight = float(node_weight.get("1.0", "end-1c"))
    return nodeName, nodeWeight


def getEdgeData():
    edgeFrom = float(add_edge_from.get("1.0", "end-1c"))
    edgeTo = float(add_edge_to.get("1.0", "end-1c"))
    edgeWeight = float(edge_weight.get("1.0", "end-1c"))
    return edgeFrom, edgeTo, edgeWeight


G = nx.DiGraph()


def AddNode():
    node_name, node_weight = getNodeData()
    G.add_node(node_name,weight=node_weight,is_goal=isGoal)
    # networkx plot
    nx.draw(G, pos, with_labels=True, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)
def AddEdge():
    from_node,to_node,weight = getEdgeData()
    G.add_edge(from_node,to_node,weight=weight)
    # networkx plot
    nx.draw(G, pos, with_labels=True, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)

# G.add_node("A", weight=0, is_goal=False)
# G.add_node("B", weight=15151, is_goal=False)
# G.add_node("C", weight=154, is_goal=False)
# G.add_node("D", weight=155, is_goal=False)
# G.add_node("E", weight=115, is_goal=False)
# G.add_node("F", weight=1, is_goal=False)
# G.add_node("G", weight=10, is_goal=True)
#
# G.add_edge("A", "B", weight=1)
# G.add_edge("A", "C", weight=2)
# G.add_edge("B", "D", weight=6)
# G.add_edge("B", "E", weight=4)
# G.add_edge("C", "F", weight=9)
# G.add_edge("C", "G", weight=7)
node_we = nx.get_node_attributes(G, 'weight')
labels = nx.get_edge_attributes(G, 'weight')
pos = graphviz_layout(G, prog="dot")

window = tk.Tk()
frame = tk.Frame(
    master=window,
    relief=tk.FLAT
)
window.title("AI algorithms visualizer")
frame.pack()

frame.columnconfigure(2, weight=1, minsize=100)
frame.rowconfigure(1, weight=1, minsize=100)

# adding nodes frames
nodes_frame = tk.Frame(
    master=frame,
    relief=tk.FLAT,
    borderwidth=3,
    padx=5,
    pady=20,
)
nodes_frame.grid(row=1, column=0, padx=20, pady=50)
guide_text = tk.Label(master=nodes_frame, text="Node name ")
guide_text.pack()
node_name = tk.Text(master=nodes_frame, width=6, height=1)
node_name.pack(pady=2)
node_weight_text = tk.Label(master=nodes_frame, text="enter the node weight")
node_weight_text.pack(pady=2)
node_weight = tk.Text(master=nodes_frame, width=6, height=1)
node_weight.pack(pady=10)
is_goal = tk.Label(master=nodes_frame, text="IS GOAL ?")
is_goal.pack()
on = tk.PhotoImage(file="on.png", )
off = tk.PhotoImage(file="off.png", )
is_goal_button = tk.Button(nodes_frame, image=off, bd=0, command=switch)
is_goal_button.pack(pady=2)
add_node = tk.Button(master=nodes_frame, text="ADD NODE", borderwidth=10,command=AddNode)
add_node.pack()
add_edge_from_text = tk.Label(master=nodes_frame, text="edge From node ")
add_edge_from_text.pack()
add_edge_from = tk.Text(master=nodes_frame, width=6, height=1)
add_edge_from.pack()
add_edge_to_text = tk.Label(master=nodes_frame, text="edge to node ")
add_edge_to_text.pack()
add_edge_to = tk.Text(master=nodes_frame, width=6, height=1)
add_edge_to.pack()
edge_weight_text = tk.Label(master=nodes_frame, text="enter the edge weight")
edge_weight_text.pack()
edge_weight = tk.Text(master=nodes_frame, width=6, height=1)
edge_weight.pack(pady=5)
add_edge = tk.Button(master=nodes_frame, text="ADD EDGE", borderwidth=10,command=AddEdge)
add_edge.pack()
hint_text = tk.Label(master=nodes_frame, text="you should add the node before add the edge !",
                     font=('Arial', 8))
hint_text.pack()
graph_frame = tk.Frame(
    master=frame,
    relief=tk.GROOVE,
    pady=5,
    padx=5
)
graph_frame.grid(row=1, column=1, padx=0, pady=5)

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, graph_frame)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
nx.draw(G, pos, with_labels=True, ax=ax1)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)

window.mainloop()
