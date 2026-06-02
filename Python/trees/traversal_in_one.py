class Node:
    # Constructor to initialize the node with a value
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


from collections import deque


def traverse(node):
    stack = deque([[node, 1]])
    preorder = []
    inorder = []
    postorder = []

    while len(stack) != 0:
        el = stack.pop()
        if el[1] == 1:
            preorder.append(el[0].data)
            el[1] += 1
            stack.append(el)
            if el[0].left:
                stack.append([el[0].left, 1])
        elif el[1] == 2:
            inorder.append(el[0].data)
            el[1] += 1
            stack.append(el)
            if el[0].right:
                stack.append([el[0].right, 1])
        else:
            postorder.append(el[0].data)

    return preorder, inorder, postorder


if __name__ == "__main__":
    tree = Node(4)
    tree.left = Node(2)
    tree.right = Node(5)
    tree.left.left = Node(3)
    tree.right.left = Node(7)
    tree.right.right = Node(6)
    tree.left.left.right = Node(9)
    tree.right.right.left = Node(8)
    tree.left.left.right.left = Node(1)

    preorder, inorder, postorder = traverse(tree)

    print(preorder, inorder, postorder)
