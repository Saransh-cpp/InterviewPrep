from collections import deque


parent_map = {}

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

def distanceK(root, target, k):
    populate_parent_map(root)
    q = deque([target])
    dist = 0
    seen = set([target])
    while q:
        size = len(q)
        if dist == k:
            break
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
    return [x.val for x in q]
