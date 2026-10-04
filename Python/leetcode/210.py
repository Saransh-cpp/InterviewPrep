from collections import deque


def findOrder(numCourses, prerequisites):
    adj_list = {i: [] for i in range(numCourses)}
    for preq in prerequisites:
        adj_list[preq[1]] += [preq[0]]

    in_edges = [0] * numCourses
    for v, edges in adj_list.items():
        for edge in edges:
            in_edges[edge] += 1

    q = deque()
    for i, edge in enumerate(in_edges):
        if edge == 0:
            q.append(i)

    top_sort = []
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            top_sort += [el]
            for v in adj_list[el]:
                in_edges[v] -= 1
                if in_edges[v] == 0:
                    q.append(v)

    return top_sort if len(top_sort) == numCourses else []
