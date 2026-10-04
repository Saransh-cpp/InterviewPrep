from collections import deque


def canFinish(numCourses, prerequisites):
    adj_list = {i: [] for i in range(numCourses)}
    for n in prerequisites:
        adj_list[n[1]] += [n[0]]

    in_edges = [0] * numCourses
    for k, v in adj_list.items():
        for val in v:
            in_edges[val] += 1

    init_zero = []
    for i, n in enumerate(in_edges):
        if n == 0:
            init_zero += [i]

    q = deque(init_zero)

    top_sort = []
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            top_sort += [el]
            for i in adj_list[el]:
                in_edges[i] -= 1
                if in_edges[i] == 0:
                    q.append(i)

    return len(top_sort) == numCourses
