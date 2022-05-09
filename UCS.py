from queue import PriorityQueue


def ucs_weight(from_node, to_node, weights=None):

    return weights.get((from_node, to_node), 10e100) if weights else 1


def ucs(graph, start, end, weights=None):

    frontier = PriorityQueue()
    frontier.put((0, start))  # (priority, node)
    explored = []

    while True:
        if frontier.empty():
            raise Exception("No way Exception")

        ucs_w, current_node = frontier.get()
        explored.append(current_node)

        if current_node == end:
            return

        for node in graph[current_node]:
            if node not in explored:
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, weights),
                    node
                ))