def deleteMiddle(head):
    if not head.next: return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = prev.next.next
    return head
