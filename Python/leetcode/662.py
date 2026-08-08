from collections import deque


def widthOfBinaryTree(root):
    q = deque([(root, 0)])
    max_width = -float("inf")
    while q:
        size = len(q)
        curr = []
        for i in range(size):
            el = q.popleft()
            curr += [el[1]]
            if el[0].left:
                q.append((el[0].left, 2 * el[1] + 1))
            if el[0].right:
                q.append((el[0].right, 2 * el[1] + 2))
        max_width = max(max_width, curr[-1] - curr[0] + 1)

    return max_width
