# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def flattenLinkedList(head):
    temp = []
    while head:
        temp += [head.val]
        t = head.child
        while t:
            temp += [t.val]
            t = t.child
        head = head.next
    temp.sort()
    head = ListNode(0)
    t = head
    for i in range(len(temp)):
        t.child = ListNode(temp[i])
        t = t.child
    return head.child

def flattenLinkedList(head):
    if not head or not head.next:
        return head
    merged_head = flattenLinkedList(head.next)
    return merge_two(head, merged_head)

def merge_two(head1, head2):
    t1 = head1
    t2 = head2
    head = ListNode(0)
    res = head
    while t1 and t2:
        if t1.val < t2.val:
            res.child = ListNode(t1.val)
            t1 = t1.child
            res = res.child
        else:
            res.child = ListNode(t2.val)
            t2 = t2.child
            res = res.child
    if t1: res.child = t1
    if t2: res.child = t2
    return head.child
