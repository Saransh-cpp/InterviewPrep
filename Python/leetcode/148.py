# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    temp = head
    temp_list = []
    while temp:
        temp_list += [temp.val]
        temp = temp.next
    temp_list.sort()
    temp = head
    i = 0
    while temp:
        temp.val = temp_list[i]
        temp = temp.next
        i += 1
    return head

def sortList(head):
    return recurse(head)

def recurse(head):
    if not head or not head.next:
        return head
    mid = find_middle(head)
    left_head = head
    right_head = mid.next
    mid.next = None
    left_head = recurse(left_head)
    right_head = recurse(right_head)
    return merge_sorted_ll(left_head, right_head)

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next
    return slow

def merge_sorted_ll(head1, head2):
    res = ListNode(0)
    curr = res
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.val < temp2.val:
            curr.next = temp1
            temp1 = temp1.next
        else:
            curr.next = temp2
            temp2 = temp2.next
        curr = curr.next
    while temp1:
        curr.next = temp1
        temp1 = temp1.next
        curr = curr.next
    while temp2:
        curr.next = temp2
        temp2 = temp2.next
        curr = curr.next
    return res.next
