def deleteDuplicates(head):
    curr = head
    while curr:
        temp = curr
        while temp.next and temp.next.val == temp.val:
            temp = temp.next
        curr.next = temp.next
        curr = curr.next
    return head
