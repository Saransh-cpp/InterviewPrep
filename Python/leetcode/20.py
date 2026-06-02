from collections import deque


def isValid(s):
    stack = deque()
    for bracket in s:
        if bracket in ["(", "{", "["]:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            if bracket == ")" and stack.pop() != "(":
                return False
            if bracket == "}" and stack.pop() != "{":
                return False
            if bracket == "]" and stack.pop() != "[":
                return False
    return len(stack) == 0
