class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    if l1 is None and l2 is None: return None

    res, carry = 0, 0
    temp = ListNode()
    head = temp

    while l1 or l2 or carry:
        res = carry
        if l1:
            res += l1.val
            l1 = l1.next
        if l2:
            res += l2.val
            l2 = l2.next
        temp.next = ListNode(res % 10)
        temp = temp.next
        carry = res // 10

    return head.next
