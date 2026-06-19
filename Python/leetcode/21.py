class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if not list1 and not list2: return None
    if not list1: return list2
    if not list2: return list1

    res = ListNode(0)
    curr = res
    while list1 and list2:
        if list1.val >= list2.val:
            curr.next = ListNode(list2.val)
            list2 = list2.next
        else:
            curr.next = ListNode(list1.val)
            list1 = list1.next
        curr = curr.next
    while list1:
        curr.next = ListNode(list1.val)
        curr = curr.next
        list1 = list1.next
    while list2:
        curr.next = ListNode(list2.val)
        curr = curr.next
        list2 = list2.next
    return res.next

def mergeTwoLists(list1, list2):
    if not list1 and not list2: return None

    res = ListNode(0)
    curr = res
    while list1 and list2:
        if list1.val >= list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        curr = curr.next
    if list1:
        curr.next = list1
    if list2:
        curr.next = list2
    return res.next
