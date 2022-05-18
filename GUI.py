import tkinter as tk
import matplotlib.pyplot as plt
from PIL.ImImagePlugin import DATE
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import ZORAAAAR
from Astar import Graph


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


def find_goal(G):
    is_Goals = nx.get_node_attributes(G, "is_goal")
    for node in is_Goals.items():
        if node[1] is True:
            # print(node[0])
            return node[0]


# start BFS
queue = []  # Initialize a queue
visited = []  # List for visited nodes.


def dfs(visited, graph, node):  # function for dfs
    our_visited = []
    visited_edges = []

    if node not in visited:
        is_Goal = nx.get_node_attributes(G, "is_goal")
        if node == is_Goal:
            return our_visited, visited_edges

        print(node)
        visited.append(node)
        our_visited.append(node)
        for neighbour in graph[node]:
            neighbour = dfs(visited, graph, neighbour)
            visited_edges.append([node, neighbour])


def bfs(visited, graph, node):  # function for BFS
    our_visited = []
    visited.append(node)
    queue.append(node)
    visited_edges = []
    is_Goal = nx.get_node_attributes(G, "is_goal")
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        our_visited.append(m)
        goal = is_Goal[m]
        if goal:
            return our_visited, visited_edges
        else:
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    visited_edges.append([m, neighbour])


def BFS_helper():
    graph = G.adj
    visited_nodes, visited_edges = bfs(visited, graph, list(graph.keys())[0])
    print(f"the visited nodes are: {visited_nodes}")
    print(f"the visited edges are: {visited_edges}")
    get_path(G)
    visualizer(visited_edges)
    showTree(True)


def Astar_helper():
    graph = graphMap(G)
    H = nx.get_node_attributes(G, 'weight')
    goal_node = find_goal(G)
    graph1 = Graph(graph, H)
    visited, edges, path = graph1.a_star_algorithm(list(graph.keys())[0], goal_node)
    print(f"the real nodes are : {visited}")
    print(f"the real edges are : {edges}")
    print(f"the real path is : {path}")
    gui_path.insert(tk.END, f"the path is {list(path)}")

    visualizer(edges,)
    showTree(True)


def greedy_helper():
    graph = graphMap(G)
    H = nx.get_node_attributes(G, 'weight')
    goal_node = find_goal(G)
    graph1 = Graph(graph, H)
    visited, edges, path = graph1.greedy_algorithm(list(graph.keys())[0], goal_node)
    print(f"the real nodes are : {visited}")
    print(f"the real edges are : {edges}")
    print(f"the real path is : {path}")
    gui_path.insert(tk.END, f"the path is {list(path)}")

    visualizer(edges)
    showTree(True)

def uniform_cost_helper():
    graph = graphMap(G)
    H = nx.get_node_attributes(G, 'weight')
    goal_node = find_goal(G)
    graph1 = Graph(graph, H)
    visited, edges, path = graph1.uniform_cost(list(graph.keys())[0], goal_node)
    print(f"the real nodes are : {visited}")
    print(f"the real edges are : {edges}")
    print(f"the real path is : {path}")
    gui_path.insert(tk.END, f"the path is {list(path)}")

    visualizer(edges)
    showTree(True)

def recurser_visualizer(visited_nodes, visited_edges, counter=0):
    max = visited_nodes[-1]
    if counter == len(visited_edges): return
    for j in range(len(visited_edges[counter]) - 1):
        if visited_edges[counter - 1][j + 1] == max: return
        nx.set_edge_attributes(G, {(visited_edges[counter][j], visited_edges[counter][j + 1]): {"color": "b"}})
        print(visited_edges[counter][j], visited_edges[counter][j + 1])

        showTree(True)

    counter += 1
    recurser_visualizer(visited_nodes, visited_edges, counter)

def visualizer(visited_edges):
    for i in range(len(visited_edges)):
        nx.set_edge_attributes(G,{(visited_edges[i][0], visited_edges[i][1]): {"color": "b"}})
        print(f"reached here {i}")
        showTree(True)

# end BFS

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


node_counter = 'A'


def getNodeData():
    global node_counter
    nodeName = node_name.get("1.0", "end-1c")
    if nodeName == "":
        nodeName = node_counter
        node_ascii = ord(node_counter)
        if node_ascii == 90:
            node_ascii += 7
        else:
            node_ascii += 1
        node_counter = chr(node_ascii)
    else:
        node_ascii = ord(nodeName)
        node_ascii += 1
        node_counter = chr(node_ascii)
    nodeWeight = float(node_weight.get("1.0", "end-1c"))
    return nodeName, nodeWeight


def getEdgeData():
    edgeFrom = add_edge_from.get("1.0", "end-1c")
    edgeTo = add_edge_to.get("1.0", "end-1c")
    edgeWeight = float(edge_weight.get("1.0", "end-1c"))
    return edgeFrom, edgeTo, edgeWeight


G = nx.DiGraph()


def deleteNode():
    node = delete_node.get("1.0", "end-1c")
    G.remove_node(node)
    showTree(True)
    print(G.adj)


def AddNode():
    if isGoal:
        color = "blue"
    else:
        color = "yellow"
    node_name, node_weight = getNodeData()
    G.add_node(node_name, weight=node_weight, is_goal=isGoal, node_color=color)
    print(DATE)
    print(G.adj)
    showTree(refresh=True)


def AddEdge():
    # if isGoal:
    #     color = "blue"
    # else:
    #     color = "yellow"
    from_node, to_node, weight = getEdgeData()
    if from_node not in nx.nodes(G) or to_node not in nx.nodes(G):
        print("node doesn't exist please add node first")
        root = tk.Tk()
        error = tk.Label(master=root, text="   node doesn't exist please add node first !!  ", font=('Arial', 20,),
                         fg="red", bg="black")
        error.pack()
        root.title("Warning!!")
        root.mainloop()
    else:
        G.add_edge(from_node, to_node, weight=weight, color='r')
    print(G.adj)
    showTree(True)


def deleteGraph():
    G.clear()
    global node_counter
    node_counter = "A"
    visited.clear()
    queue.clear()
    gui_path.delete('1.0', tk.END)

    showTree(True)


def get_path(G):
    goal_node = [x for x, y in G.nodes(data=True) if y['is_goal'] == True]
    print(f"goal node is {goal_node}")
    path = []
    starting_node = list(G.adj.keys())[0]
    path.append(goal_node[0])
    while starting_node not in path:

        for nodes in G.predecessors(path[-1]):
            path.append(nodes)
    print(path)
    gui_path.insert(tk.END, f"the path is {list(reversed(path))}")
    return list(reversed(path))


# def path_helper():
#     goal_node = [x for x, y in G.nodes(data=True) if y['is_goal'] == True]
#     print(f"goal node is: {goal_node}")
#     print(get_path(G,goal_node))

# def update_Path():
#     Path = get_path(G)
#     gui_path.insert(tk.END,f"the path is {Path}")
#     print(gui_path)

#
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

window = tk.Tk()
frame = tk.Frame(
    master=window,
    relief=tk.FLAT
)
window.title("AI algorithms visualizer")
frame.pack()

frame.columnconfigure(3, weight=1, minsize=100)
frame.rowconfigure(1, weight=1, minsize=100)

# adding nodes frames
nodes_frame = tk.Frame(
    master=frame,
    relief=tk.FLAT,
    borderwidth=3,
    padx=5,
    pady=10,
)
additional_frame = tk.Frame(
    master=frame,
    relief=tk.FLAT,
    borderwidth=3,
    padx=5,
    pady=10
)
nodes_frame.grid(row=1, column=0, padx=20, pady=50)
additional_frame.grid(row=1, column=1)
guide_text = tk.Label(master=nodes_frame, text="Node name ")
guide_text.pack()
node_name = tk.Text(master=nodes_frame, width=6, height=1)
# node_name.insert(tk.END,"A")
node_name.pack(pady=2)
node_weight_text = tk.Label(master=nodes_frame, text="enter the node weight")
node_weight_text.pack(pady=2)
node_weight = tk.Text(master=nodes_frame, width=6, height=1)
node_weight.insert(tk.END, "0")
node_weight.pack(pady=10)
is_goal = tk.Label(master=nodes_frame, text="IS GOAL ?")
is_goal.pack()
on = tk.PhotoImage(file="on.png", )
off = tk.PhotoImage(file="off.png", )
is_goal_button = tk.Button(nodes_frame, image=off, bd=0, command=switch)
is_goal_button.pack(pady=2)
add_node = tk.Button(master=nodes_frame, text="ADD NODE", borderwidth=10, command=AddNode)
add_node.pack()
auto_graph = tk.Button(master=additional_frame, text="Auto Graph", borderwidth=10, command=ZORAAAAR.node_statics)
auto_graph.pack(pady=10)
hint_text = tk.Label(master=nodes_frame, text="warning you should add the node before adding the edge !",
                     font=('Arial', 8,), fg="red", bg="black")
hint_text.pack(pady=5)
add_edge_from_text = tk.Label(master=additional_frame, text="edge From node ")
add_edge_from_text.pack()
add_edge_from = tk.Text(master=additional_frame, width=6, height=1)
add_edge_from.insert(tk.END, "A")
add_edge_from.pack()
add_edge_to_text = tk.Label(master=additional_frame, text="edge to node ")
add_edge_to_text.pack()
add_edge_to = tk.Text(master=additional_frame, width=6, height=1)
add_edge_to.insert(tk.END, "B")
add_edge_to.pack()
edge_weight_text = tk.Label(master=additional_frame, text="enter the edge weight")
edge_weight_text.pack()
edge_weight = tk.Text(master=additional_frame, width=6, height=1)
edge_weight.insert(tk.END, "1")
edge_weight.pack(pady=5)
add_edge = tk.Button(master=additional_frame, text="ADD EDGE", borderwidth=10, command=AddEdge)
add_edge.pack()

delete_node_text = tk.Label(master=nodes_frame, text="enter the node to be deleted")
delete_node_text.pack()
delete_node = tk.Text(master=nodes_frame, width=6, height=1)
delete_node.pack(pady=5)
delete_node_button = tk.Button(master=nodes_frame, text="Delete Node", borderwidth=10, command=deleteNode)
delete_node_button.pack()
rest_button = tk.Button(master=nodes_frame, text="RESET GRAPH", pady=5, padx=5, borderwidth=9, relief=tk.GROOVE,
                        width=20, bg='orange'
                        , command=deleteGraph)
rest_button.pack(pady=9)
algos_menu_frame = tk.Frame(
    master=additional_frame,
    relief=tk.RIDGE,
    borderwidth=15
)
algos_menu_frame.pack(pady=1)
algos_menu = tk.Menubutton(master=algos_menu_frame, text="choose algorithm", bg="blue", fg="yellow")
algos_menu.menu = tk.Menu(algos_menu)
algos_menu["menu"] = algos_menu.menu
algos_menu.menu.add_command(label="Breadth first", command=BFS_helper)
algos_menu.menu.add_command(label="depth first", )
algos_menu.menu.add_command(label="Iterative deepening", )
algos_menu.menu.add_command(label="Uniform Cost",command=uniform_cost_helper )
algos_menu.menu.add_command(label="A*", command=Astar_helper)
algos_menu.menu.add_command(label="Greedy",command=greedy_helper )
algos_menu.pack()

gui_path = tk.Text(additional_frame, height=5,
                   width=25,
                   bg="light cyan",
                   # state='disabled'
                   )
gui_path.pack(pady=10)

graph_frame = tk.Frame(
    master=frame,
    relief=tk.GROOVE,
    pady=0,
    padx=5
)
graph_frame.grid(row=1, column=2, padx=0, pady=0)


def showTree(refresh=False):
    if refresh:
        graph_frame.destroy()
        graph_frame.__init__(master=frame, )
        graph_frame.grid(row=1, column=2, pady=5, padx=0)
        figure1 = plt.Figure()
        ax1 = figure1.add_subplot()
        bar1 = FigureCanvasTkAgg(figure1, graph_frame)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        node_we = nx.get_node_attributes(G, 'weight')
        labels = nx.get_edge_attributes(G, 'weight')
        pos = graphviz_layout(G, prog="dot")
        node_colors = nx.get_node_attributes(G, 'node_color')
        colors = []
        for color in node_colors.values():
            colors.append(color)
        edges = G.edges()
        edge_colors = [G[u][v]['color'] for u, v in edges]
        nx.draw(G, pos, with_labels=True, ax=ax1, node_color=colors, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)
    else:
        figure1 = plt.Figure()
        ax1 = figure1.add_subplot()
        bar1 = FigureCanvasTkAgg(figure1, graph_frame)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        node_we = nx.get_node_attributes(G, 'weight')
        labels = nx.get_edge_attributes(G, 'weight')
        pos = graphviz_layout(G, prog="dot")
        node_colors = nx.get_node_attributes(G, 'node_color')
        edge_colors = nx.get_edge_attributes(G, 'edge_color')
        colors = []
        for color in node_colors.values():
            colors.append(color)
        print(f"this is colors list: {colors}")
        nx.draw(G, pos, with_labels=True, ax=ax1, node_color=colors, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)


showTree()

# window.state('zoomed')
window.mainloop()
