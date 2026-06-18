def rotateRight(head, k):
    if head is None: return None

    curr = head
    ln = 0
    while curr.next:
        ln += 1
        curr = curr.next
    if ln + 1 == k: return head
    curr.next = head
    ln += 1
    curr = head

    for _ in range(ln - (k % ln) - 1):
        curr = curr.next

    head = curr.next
    curr.next = None
    return head
