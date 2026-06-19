def getIntersectionNode(headA, headB):
    lA = headA
    lB = headB
    lenA = 0
    lenB = 0
    while lA:
        lenA += 1
        lA = lA.next
    while lB:
        lenB += 1
        lB = lB.next
    lenDiff = abs(lenA - lenB)
    if lenA > lenB:
        for _ in range(lenDiff):
            headA = headA.next
    else:
        for _ in range(lenDiff):
            headB = headB.next
    while headA and headB:
        if headA == headB: return headA
        headA = headA.next
        headB = headB.next
    return None

def getIntersectionNode(headA, headB):
    lA = headA
    lB = headB
    while lA != lB:
        lA = lA.next
        lB = lB.next
        if lA == lB: return lA
        if not lB:
            lB = headA
        if not lA:
            lA = headB
    return lA
