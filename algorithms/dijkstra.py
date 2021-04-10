def dijkstra(graph, start, fin):
    processed = []
    parents = {}
    costs = {}
    infinity = float("inf")

    for node in graph:
        costs[node] = infinity
        parents[node] = None
    costs[start] = 0
    parents[start] = None
    for node in graph[start]:
        costs[node] = graph[start][node]
        parents[node] = start

    def find_next_node():
        minimum = infinity
        next_node = None
        for node in graph:
            if (costs[node] < minimum) and (not node in processed):
                minimum = costs[node]
                next_node = node
        return next_node

    node = find_next_node()
    while node is not None:
        for child in graph[node]:
            if costs[child] is None or costs[child] > costs[node] + graph[node][child]:
                costs[child] = costs[node] + graph[node][child]
                parents[child] = node
        processed.append(node)
        node = find_next_node()

    print('min cost:', costs[fin])

    path = [fin]
    while parents[path[0]] is not None:
        path.insert(0, parents[path[0]])
    path_str = path[0]
    for node in path[1:]:
        path_str += ' -> ' + node
    print('path: ', path_str)


graph = {}
graph["start"] = {'a': 6, 'b': 2}
graph["a"] = {'fin': 1}
graph["b"] = {'fin': 5, 'a': 3}
graph["fin"] = {}

dijkstra(graph, 'start', 'fin')

graph2 = {
    'start': {'a': 5, 'b': 2},
    'a': {'c': 4, 'd': 2},
    'b': {'a': 8, 'd': 7},
    'c': {'d': 6, 'fin': 3},
    'd': {'fin': 1},
    'fin': {},
}

dijkstra(graph2, 'start', 'fin')
