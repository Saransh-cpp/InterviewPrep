from collections import deque


def invertTree(root):
    if not root:
        return

    q = deque([root])
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            left = None
            right = None
            if el.left:
                q.append(el.left)
                left = el.left
            if el.right:
                q.append(el.right)
                right = el.right
            if left and right:
                el.left, el.right = el.right, el.left
            elif left:
                el.right = el.left
                el.left = None
            else:
                el.left = el.right
                el.right = None
    return root
