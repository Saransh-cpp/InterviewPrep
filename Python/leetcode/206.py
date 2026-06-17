def reverseList(head):
    if head is None: return None
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
