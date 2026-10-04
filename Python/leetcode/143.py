def reverse(head):
    back = None
    while head:
        front = head.next
        head.next = back
        back = head
        head = front
    return back

def reorderList(head):
    if not head.next: return head

    slow = head
    fast = head
    prev = slow
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = None
    reversed_ll = reverse(slow)

    ll = head
    prev = ll
    while ll and reversed_ll:
        temp1 = ll.next
        ll.next = reversed_ll
        temp2 = reversed_ll.next
        reversed_ll.next = temp1
        ll = temp1
        prev = reversed_ll
        reversed_ll = temp2
    if reversed_ll:
        prev.next = reversed_ll
    return head
