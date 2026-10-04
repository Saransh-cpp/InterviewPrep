from collections import deque


def topsort(graph, in_edges, top):
    q = deque()
    for i, in_edge in enumerate(in_edges):
        if in_edge == 0:
            q.append(i)
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            top += [el]
            for e in graph[el]:
                in_edges[e] -= 1
                if in_edges[e] == 0:
                    q.append(e)

def eventualSafeNodes(graph):
    rev = [[] for _ in range(len(graph))]
    in_edges = [0] * len(graph)
    for i in range(len(graph)):
        for e in graph[i]:
            rev[e] += [i]
            in_edges[i] += 1

    top = []
    topsort(rev, in_edges, top)
    return sorted(top)
