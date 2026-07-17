def removeElements(head, val):
    if not head: return None
    temp = head
    while temp.next:
        if temp.next.val == val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head.next if head and head.val == val else head
