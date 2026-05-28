class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def insert(head, data):
    return Node(data, head)


if __name__ == "__main__":
    a = Node(5, None)
    b = Node(6, a)
    c = Node(7, b)

    d = insert(c, 8)

    tail = d
    while tail:
        print(tail.data, "->", end=" ")
        tail = tail.next
