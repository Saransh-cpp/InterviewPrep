def oddEvenList(head):
    if head is None: return None
    if head.next is None: return head

    ll1 = head
    ll2_head = head.next
    ll2 = head.next
    while ll1 and ll2 and (ll1.next and ll2.next):
        ll1.next = ll1.next.next
        ll2.next = ll2.next.next
        ll1 = ll1.next
        ll2 = ll2.next
    ll1.next = ll2_head
    return head
