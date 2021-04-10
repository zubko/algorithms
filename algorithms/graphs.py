def is_seller(name):
    return name[-1] == 'm'


def breadth_first_search(graph):
    queue = [] + graph['you']
    i = 0
    while i < len(queue):
        friend = queue[i]
        if is_seller(friend):
            print('Found ' + friend + ' is a seller')
            return True
        else:
            queue += [f for f in graph[friend] if not f in queue]
            i += 1
    print('Not found.')
    return False


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

breadth_first_search(graph)
