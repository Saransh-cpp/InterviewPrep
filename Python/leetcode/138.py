class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    d = {}
    curr = head
    res = Node(0)
    res_curr = res

    while curr:
        res_curr.next = Node(curr.val)
        d[curr] = res_curr.next
        res_curr = res_curr.next
        curr = curr.next

    curr = head
    res = res.next
    res_curr = res

    while curr:
        res_curr.random = d.get(curr.random, None)
        curr = curr.next
        res_curr = res_curr.next

    return res

def copyRandomList(head):
    if head is None: return None

    curr = head
    while curr:
        temp = curr.next
        curr.next = Node(curr.val, temp)
        curr = curr.next.next

    curr = head
    while curr:
        curr.next.random = None if not curr.random else curr.random.next
        curr = curr.next.next

    curr = head
    while curr.next.next:
        temp = curr.next.next
        curr.next.next = curr.next.next.next
        curr = temp

    return head.next
