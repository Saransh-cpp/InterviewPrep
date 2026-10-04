from collections import deque


def numIslands(grid):
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and not visited[i][j]:
                islands += 1
                visited[i][j] = 1
                q = deque([(i, j)])
                while q:
                    size = len(q)
                    print(size)
                    for _ in range(size):
                        m, n = q.popleft()
                        if n > 0 and grid[m][n - 1] == "1":
                            if not visited[m][n - 1]:
                                q.append((m, n - 1))
                                visited[m][n - 1] = 1
                        if m > 0 and grid[m - 1][n] == "1":
                            if not visited[m - 1][n]:
                                q.append((m - 1, n))
                                visited[m - 1][n] = 1
                        if m < len(grid) - 1 and grid[m + 1][n] == "1":
                            if not visited[m + 1][n]:
                                q.append((m + 1, n))
                                visited[m + 1][n] = 1
                        if n < len(grid[0]) - 1 and grid[m][n + 1] == "1":
                            if not visited[m][n + 1]:
                                q.append((m, n + 1))
                                visited[m][n + 1] = 1
    return islands
