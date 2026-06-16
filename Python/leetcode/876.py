def middleNode(head):
    if head is None or head.next is None: return head

    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    i = 0
    while i != length // 2:
        head = head.next
        i += 1
    return head

def middleNode(head):
    if head is None or head.next is None: return head

    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
