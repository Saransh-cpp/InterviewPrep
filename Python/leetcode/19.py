def removeNthFromEnd(head, n):
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        head = head.next
    else:
        while fast.next:
            slow = slow.next
            fast = fast.next

        if slow.next:
            slow.next = slow.next.next
        else:
            head = None

    return head
