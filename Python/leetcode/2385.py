from collections import deque


parent_map = {}
node = None

def populate_parent_map(root):
    q = deque([root])
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            if el.left:
                parent_map[el.left] = el
                q.append(el.left)
            if el.right:
                parent_map[el.right] = el
                q.append(el.right)

def get_node(root, start):
    if not root:
        return
    if root.val == start:
        node = root
    get_node(root.left, start)
    get_node(root.right, start)

def amountOfTime(root, start):
    populate_parent_map(root)
    get_node(root, start)
    q = deque([node])
    dist = 0
    seen = set([node])
    while q:
        size = len(q)
        for _ in range(size):
            el = q.popleft()
            if el.left and el.left not in seen:
                q.append(el.left)
                seen.add(el.left)
            if el.right and el.right not in seen:
                q.append(el.right)
                seen.add(el.right)
            if parent_map.get(el, None) and parent_map[el] not in seen:
                q.append(parent_map[el])
                seen.add(parent_map[el])
        dist += 1
    return dist - 1
