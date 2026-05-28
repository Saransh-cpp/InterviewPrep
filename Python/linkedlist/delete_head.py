class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def delete_head(head):
    if head is None: return None
    temp = head
    head = head.next
    del temp
    return head


if __name__ == "__main__":
    a = Node(5, None)
    b = Node(6, a)
    c = Node(7, b)

    d = delete_head(c)

    tail = d
    while tail:
        print(tail.data, "->", end=" ")
        tail = tail.next
