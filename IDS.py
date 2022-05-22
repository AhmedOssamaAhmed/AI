
def dls( graph, node,G,maxdepth):  # function for BFS
    queue=[]
    our_visited = []
    visited = []
    visited.append(node)
    queue.append((node, [node], 0))
    visited_edges = []
    # is_Goal = nx.get_node_attributes(G, "is_goal")
    while len(queue) > 0:
        m = None
        selectedPath = []
        selectedDepth = -1
        selectedIndex = -1
        i = 0
        for (node, path, depth) in queue:
            if selectedDepth < depth:
                selectedDepth = depth
                m = node
                selectedPath = path
                selectedIndex = i
            i+=1
        queue.pop(selectedIndex)
        our_visited.append(m)
        visited_edges.append([selectedPath[len(selectedPath) -2], m])
        if m == G:
            return our_visited, visited_edges, selectedPath
        else:
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    if selectedDepth < maxdepth:
                        queue.append((neighbour, selectedPath + [neighbour], selectedDepth + 1))
    return our_visited, visited_edges, []

def iddls(graph, node,G):
    i = 0
    path = []
    while len(path) == 0:
        our_visited, visited_edges, path = dls(graph, node,G, i)
        i+=1
    return our_visited, visited_edges, path