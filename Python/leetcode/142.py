def detectCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = head
            break
    if not fast or not fast.next:
        return None
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow
