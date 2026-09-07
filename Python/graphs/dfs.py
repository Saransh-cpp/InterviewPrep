def recurse(graph, node_val, visited, result):
    result += [node_val]
    visited[node_val] = 1
    for neigbour in graph[node_val]:
        if not visited[neigbour]:
            recurse(graph, neigbour, visited, result)

def dfs(graph, len_graph):
    res = []
    visited = [0] * len_graph
    for node in range(len(len_graph)):
        if not visited[node]:
            recurse(graph, node, [], res)
    return res
