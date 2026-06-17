def isPalindrome(head):
    if head is None: return False

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    temp = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    while prev:
        if prev.val != head.val: return False
        prev = prev.next
        head = head.next

    return True
