import GUI


def node_statics():
    GUI.G
    GUI.G.add_node("A", weight=9, is_goal=False,node_color="yellow")
    GUI.G.add_node("B", weight=7, is_goal=False,node_color="yellow")
    GUI.G.add_node("C", weight=3, is_goal=False,node_color="yellow")
    GUI.G.add_node("D", weight=4, is_goal=False,node_color="yellow")
    GUI.G.add_node("E", weight=0, is_goal=True,node_color="blue")
    GUI.G.add_node("F", weight=6, is_goal=False,node_color="yellow")
    GUI.G.add_node("G", weight=7, is_goal=False,node_color="yellow")
    GUI.G.add_node("H", weight=5, is_goal=False,node_color="yellow")
    GUI.G.add_node("I", weight=4, is_goal=False,node_color="yellow")
    GUI.G.add_node("J", weight=4, is_goal=False,node_color="yellow")

    GUI.G.add_edge("A", "B", weight=1,color='r')
    GUI.G.add_edge("A", "C", weight=2,color='r')
    GUI.G.add_edge("A", "D", weight=6,color='r')
    GUI.G.add_edge("C", "I", weight=4,color='r')
    GUI.G.add_edge("C", "F", weight=9,color='r')
    GUI.G.add_edge("C", "G", weight=7,color='r')
    GUI.G.add_edge("D", "E", weight=7,color='r')
    GUI.G.add_edge("D", "H", weight=7,color='r')
    GUI.G.add_edge("D", "J", weight=7,color='r')
    GUI.showTree(True)