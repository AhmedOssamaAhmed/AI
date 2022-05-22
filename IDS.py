Visited_edges_list = []
Visited = []
path_list=[]
temp_VEdges=[]
iterativeVisited=[]
def graphMapIDS(graph):
    #used to change the list presented by the user to a another form for the IDDFS
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
            major_list.append(minor_key)
        our_dict.update({major_key: major_list})
        # print(our_dict)
    return our_dict

def DLS(graph, src, target, maxDepth):
    global iterativeVisited
    global Visited
    global temp_VEdges
    # temp=[]
    # temp_VEdges=[]

    Visited.append(src)
    if src == target:
        return True
    # If reached the maximum depth, stop recursing.
    if maxDepth <= 0: return False

    # Recur for all the vertices adjacent to this vertex
    for i in graph[src]:
        if(graph[i] not in iterativeVisited):
            temp=[]
            temp.append(src)
            temp.append(i)
            temp_VEdges.append(temp)
            print(f"temp_edges{temp_VEdges}")
        else:
            break

        if (DLS(graph, i, target, maxDepth - 1)):
            return True
    return False

def IDDFS_Driver(grapher, src, target, maxDepth):
    global Visited
    global path_list
    global temp_VEdges
    graph = graphMapIDS(grapher)
    # graph = {'A':['B','C'],'B':['D','E'],'C':['F','G']}
    if IDDFS(graph, src, target, maxDepth):
        path_list.append(target)
        # get_key(target, graph)
        print(f"our visitedddd {Visited}")
        adjusted_visited = []
        for i in range(len(Visited)-1,0,-1):
            if Visited[i] == src:
                adjusted_visited.append(Visited[i])
                print(Visited[i])
                print("Testtttt")
                print(src)
                return list(reversed(adjusted_visited)),temp_VEdges
                    # ,get_visited_edges(Visited, graph, target, src)
            else:
                print(Visited[i])
                adjusted_visited.append(Visited[i])
        # return (list(reversed(path_list))),adjusted_visited,get_visited_edges(Visited, graph, target, src)

    else:
        print("Unreachable")
def IDDFS(graph, src, target, maxDepth):
    for i in range(maxDepth):
        Reachable = (DLS(graph, src, target, i))
        if Reachable:
            break
    return Reachable
def get_key(val, my_dict):
    global path_list
    for key, value in my_dict.items():
        if val in value:
            path_list.append(key)
            get_key(key, my_dict)
            print(path_list)
def get_visited_edges(Visited , my_dict, target, start_node):
    global Visited_edges_list
    state = False
    if target not in Visited:
        return
    else:
        temp2 = target
        for i in range(len(Visited)):
            # if state:
            #     break
            temp = []
            for key, value in my_dict.items():
                # print("first line after for")
                # if temp2 is start_node:
                #     state = True
                if temp2 in value:
                    temp.append(key)
                    temp.append(temp2)
                    print(Visited_edges_list)
                    if temp not in Visited_edges_list:
                        Visited_edges_list.append(temp)
                        temp2=key
                    break
    return list(reversed(Visited_edges_list))
