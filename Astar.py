
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

    def a_star_algorithm(self, startnode, endnode):
        parents = {}
        parents[startnode] = startnode
        path = []
        visitednode = []
        edgelist = []
        min = startnode
        minPath = [startnode]
        minCost = 0
        fringe = []
        while True:
            visitednode.append(min)
            if min != startnode:
                edgelist.append([minPath[len(minPath) - 2], min])
            if min == endnode:
                path = minPath
                break
            next = self.get_neighbors(min)
            for node in next:
                fringe += [(node[0], minCost + node[1], minPath + [node[0]])]
            minHeuristic = 9999999
            for n in fringe:
                if n[0] not in visitednode:
                    if self.h(n[0])+n[1] < minHeuristic:
                        minHeuristic = self.h(n[0]) + n[1]
                        minCost = n[1]
                        min = n[0]
                        minPath = n[2]
        return visitednode, edgelist, path

    def greedy(self, startnode, endnode):
        parents = {}
        parents[startnode] = startnode
        path = []
        visitednode = []
        edgelist = []
        min = startnode
        minPath = [startnode]
        fringe =[]
        while True:
            visitednode.append(min)
            if min != startnode:
                edgelist.append([minPath[len(minPath)-2],min])
            if min == endnode:
                path = minPath
                break
            next = self.get_neighbors(min)
            for node in next:
                fringe += [(node[0],node[1], minPath + [node[0]])]
                print("fringe like")
                print(fringe)
            minHeuristic = 9999999
            for n in fringe:
                if n[0] not in visitednode:
                    if self.h(n[0]) < minHeuristic:
                        minHeuristic = self.h(n[0])
                        min = n[0]
                        minPath = n[2]
        return edgelist, path

    def uniform_cost(self, startnode, endnode):
        parents = {}
        parents[startnode] = startnode
        path = []
        visitednode = []
        openlist = []
        g = {}
        # edgelist=[]
        edgelist2 = []
        reconst_path = [endnode]

        openlist.append(startnode)
        for v in self.adjacency_list:
            for (m, weight) in self.get_neighbors(v):
                if v == startnode:
                    g[v] = 0
                    g[m] = weight
                    path.append(startnode)
                    parents[m] = startnode

                    openlist.append(m)
                else:
                    if m not in g:
                        g[m] = g[v] + weight
                        openlist.append(m)
                        parents[m] = v

        min = startnode
        while min != endnode:

            value_k = (g[openlist[0]])
            for n in openlist:
                value_k1 = g[n]

                if value_k >= value_k1:
                    min = n
                    value_k = value_k1
            if value_k > g[openlist[0]]:
                min = openlist[0]

            openlist.remove(min)
            path.append(min)
            if min not in visitednode:
                visitednode.append(min)
        for l in range(len(visitednode)):
            if visitednode[l] != startnode:
                edgelist = []
                # print(parents[l])
                edgelist.append(parents[visitednode[l]])
                edgelist.append(visitednode[l])
                # edgelist.append(min)
                edgelist2.append(edgelist)
        n = endnode
        if n == endnode:

            while parents[n] != n:
                reconst_path.append(parents[n])
                n = parents[n];

        reconst_path.reverse()
        print(visitednode)
        print('Visited edges: {}'.format(edgelist2))
        print('Path found: {}'.format(reconst_path))
        return edgelist2,reconst_path

