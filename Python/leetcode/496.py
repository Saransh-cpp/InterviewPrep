from collections import deque


def nextGreaterElement(nums1, nums2):
    m_stack = deque()
    res = {}
    for i in range(len(nums2) - 1, -1, -1):
        if len(m_stack) == 0: res[nums2[i]] = -1
        else:
            p = m_stack[-1]
            while nums2[i] >= p and p != -1:
                m_stack.pop()
                p = -1 if len(m_stack) == 0 else m_stack[-1]
            res[nums2[i]] = p
        m_stack.append(nums2[i])
    ret = []
    for i in range(len(nums1)):
        ret.append(res[nums1[i]])
    return ret
