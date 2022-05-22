import GUI

def node_statics2():
    GUI.G
    GUI.G.add_node("S", weight=13, is_goal=False, node_color="yellow")
    GUI.G.add_node("A", weight=12, is_goal=False, node_color="yellow")
    GUI.G.add_node("B", weight=4, is_goal=False, node_color="yellow")
    GUI.G.add_node("C", weight=7, is_goal=False, node_color="yellow")
    GUI.G.add_node("D", weight=3, is_goal=False, node_color="yellow")
    GUI.G.add_node("E", weight=8, is_goal=False, node_color="yellow")
    GUI.G.add_node("F", weight=2, is_goal=False, node_color="yellow")
    GUI.G.add_node("I", weight=9, is_goal=False, node_color="yellow")
    GUI.G.add_node("G", weight=0, is_goal=True, node_color="blue")
    GUI.G.add_node("H", weight=4, is_goal=False, node_color="yellow")

    GUI.G.add_edge("S", "A", weight=3, color='r')
    GUI.G.add_edge("A", "C", weight=4, color='r')
    GUI.G.add_edge("A", "D", weight=1, color='r')
    GUI.G.add_edge("S", "B", weight=2, color='r')
    GUI.G.add_edge("B", "E", weight=3, color='r')
    GUI.G.add_edge("B", "F", weight=1, color='r')
    GUI.G.add_edge("E", "H", weight=5, color='r')
    GUI.G.add_edge("F", "I", weight=2, color='r')
    GUI.G.add_edge("F", "G", weight=3, color='r')
    # GUI.G.add_edge("I", "H", weight=12, color='r')
    # GUI.G.add_edge("I", "J", weight=1, color='r')
    # GUI.G.add_edge("I", "K", weight=1, color='r')
    GUI.showTree(True)
