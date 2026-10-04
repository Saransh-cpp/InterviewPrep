from collections import deque


def biparty(graph, start, bip):
    q = deque([start])
    col = 0
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            if bip[el] == -1:
                bip[el] = int(col)
                for v in graph[el]:
                    q.append(v) 
            else:
                for v in graph[el]:
                    if bip[v] == bip[el]:
                        return False
        col = not col
    return True

def isBipartite(graph):
    bip = [-1] * len(graph)
    for i in range(len(graph)):
        if bip[i] == -1:
            is_bip = biparty(graph, i, bip)
            if not is_bip:
                return is_bip
    return True
