class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def delete_tail(head):
    while head:
        if head.next.next is None:
            head.next = None
            return
        head = head.next


def delete_tail(head):
    if head is None or head.next is None:
        return None

    # needed as single-node case changes what the head is
    curr = head
    while curr.next.next is not None:
        curr = curr.next

    # Delete tail node
    curr.next = None
    return curr


if __name__ == "__main__":
    a = Node(5, None)
    b = Node(6, a)
    c = Node(7, b)

    delete_tail(c)

    tail = c
    while tail:
        print(tail.data, "->", end=" ")
        tail = tail.next
