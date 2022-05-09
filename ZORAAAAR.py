import GUI


def node_statics():
    GUI.G
    GUI.G.add_node("A", weight=15121, is_goal=False,node_color="yellow")
    GUI.G.add_node("B", weight=15151, is_goal=False,node_color="yellow")
    GUI.G.add_node("C", weight=154, is_goal=False,node_color="yellow")
    GUI.G.add_node("D", weight=155, is_goal=False,node_color="yellow")
    GUI.G.add_node("E", weight=115, is_goal=True,node_color="blue")
    GUI.G.add_node("F", weight=1, is_goal=False,node_color="yellow")
    GUI.G.add_node("G", weight=10, is_goal=False,node_color="yellow")

    GUI.G.add_edge("A", "B", weight=1,color='r')
    GUI.G.add_edge("A", "C", weight=2,color='r')
    GUI.G.add_edge("B", "D", weight=6,color='r')
    GUI.G.add_edge("B", "E", weight=4,color='r')
    GUI.G.add_edge("C", "F", weight=9,color='r')
    GUI.G.add_edge("C", "G", weight=7,color='r')
    GUI.showTree(True)