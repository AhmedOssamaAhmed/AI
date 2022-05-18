# import networkx as nx
# from matplotlib import pyplot as plt
# from networkx.drawing.nx_pydot import graphviz_layout

# G = nx.DiGraph()
# G.add_node("A", weight=5, is_goal=False)
# G.add_node("B", weight=4, is_goal=False)
# G.add_node("C", weight=3, is_goal=False)
# G.add_node("D", weight=0, is_goal=True)
# G.add_node("E", weight=9, is_goal=False)
# G.add_node("F", weight=1, is_goal=False)
# G.add_node("G", weight=6, is_goal=False)
#
# G.add_edge("A", "B", weight=1)
# G.add_edge("A", "C", weight=2)
# G.add_edge("B", "D", weight=6)
# G.add_edge("B", "E", weight=4)
# G.add_edge("C", "F", weight=9)
# G.add_edge("C", "G", weight=7)
#
# node_we = nx.get_node_attributes(G, 'weight')
# labels = nx.get_edge_attributes(G, 'weight')
# pos = graphviz_layout(G, prog="dot")
# nx.draw(G, pos, with_labels=True)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


# print(node_we)
# plt.show()

class Graph:

    def __init__(self, adjacency_list, H):
        self.adjacency_list = adjacency_list
        self.H = H

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

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):

        return self.H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        Visited = [stop_node]
        Visited_edges = []

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                Visited.append(start_node)
                Visited.reverse()
                for i in range(len(Visited)):
                    if Visited[i] != start_node:
                        list = []
                        list.append(parents[Visited[i]])
                        list.append(Visited[i])
                        Visited_edges.append(list)

                reconst_path.reverse()
                print('Visited: {}'.format(Visited))
                print('Visited edges: {}'.format(Visited_edges))
                print('Path found: {}'.format(reconst_path))
                return Visited, Visited_edges, reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)
            if parents[m] in closed_list:
                if parents[m] != start_node:
                    Visited.append(parents[m])
            if m in closed_list:
                Visited.append(m)

        print('Path does not exist!')
        return None

    def greedy_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        Visited = [stop_node]
        Visited_edges = []

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or  self.h(v) <  self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                Visited.append(start_node)
                Visited.reverse()
                for i in range(len(Visited)):
                    if Visited[i] != start_node:
                        list = []
                        list.append(parents[Visited[i]])
                        list.append(Visited[i])
                        Visited_edges.append(list)

                reconst_path.reverse()
                print('Visited: {}'.format(Visited))
                print('Visited edges: {}'.format(Visited_edges))
                print('Path found: {}'.format(reconst_path))
                return Visited, Visited_edges, reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] =  weight

                else:
                    if g[m] >  weight:
                        g[m] =  weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)
            if parents[m] in closed_list:
                if parents[m] != start_node:
                    Visited.append(parents[m])
            if m in closed_list:
                Visited.append(m)

        print('Path does not exist!')
        return None

    def uniform_cost(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        Visited = [stop_node]
        Visited_edges = []

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v]  < g[n] :
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                Visited.append(start_node)
                Visited.reverse()
                for i in range(len(Visited)):
                    if Visited[i] != start_node:
                        list = []
                        list.append(parents[Visited[i]])
                        list.append(Visited[i])
                        Visited_edges.append(list)

                reconst_path.reverse()
                print('Visited: {}'.format(Visited))
                print('Visited edges: {}'.format(Visited_edges))
                print('Path found: {}'.format(reconst_path))
                return Visited, Visited_edges, reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n]

                else:
                    if g[m] > g[n] :
                        g[m] = g[n]
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)
            if parents[m] in closed_list:
                if parents[m] != start_node:
                    Visited.append(parents[m])
            if m in closed_list:
                Visited.append(m)

        print('Path does not exist!')
        return None


# def graphMap(graph):
#     first_dict = graph.adj
#     graph_len = len(list(first_dict.items()))
#     our_dict = {}
#     # looping on the whole graph
#     for j in range(graph_len):
#         major_key = list(first_dict.items())[j][0]
#         value = list(first_dict.items())[j][1]
#         # second loop making tuples
#         major_list = []
#         for i in range(len(value)):
#             minor_key = list(value.items())[i][0]
#             minor_value_helper = list(value.items())[i][1]
#             minor_value = list(minor_value_helper.items())[0][1]
#             arr = []
#             arr.append(minor_key)
#             arr.append(minor_value)
#             arr = tuple(arr)
#             major_list.append(arr)
#             # print(major_list)
#         our_dict.update({major_key: major_list})
#         # print(our_dict)
#     return our_dict
#
# def find_goal(G):
#     is_Goal = nx.get_node_attributes(G, "is_goal")
#     for node in is_Goal.items():
#         if node[1] is True:
#             # print(node[0])
#             return node[0]


# if __name__ == "__main__":
    # adjacency_list = {
    #     'A': [('B', 2), ('C', 2)],
    #     'B': [('D', 2), ('E', 2)],
    #     'C': [('F', 2), ('G', 2)]
    # }
    # H = {
    #     'A': 5,
    #     'B': 4,
    #     'C': 6,
    #     'D': 3,
    #     'E': 0,
    #     'F': 7,
    #     'G': 8
    # }

    # print(G.edges)
    # G.adjacency()
    # for node in G.adjacency():
    #     print(node)
    # print(G.adj)

    # graph = graphMap(G)
    # H = nx.get_node_attributes(G, 'weight')
    # goal_node = find_goal(G)
    # graph1 = Graph(graph, H)
    # visited, edges, path = graph1.a_star_algorithm(list(graph.keys())[0], goal_node)
    # print(f"our visited is: {visited}")
    # print(f"our edges are: {edges}")
    # print(f"our path is: {path}")
