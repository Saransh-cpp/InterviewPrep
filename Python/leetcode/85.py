from collections import deque


def nextSmallestElement(arr):
    st = deque()
    n = len(arr)
    nse = [n] * n
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        if st:
            nse[i] = st[-1]
        st.append(i)
    return nse

def prevSmallestElement(arr):
    st = deque()
    n = len(arr)
    pse = [-1] * n
    for i in range(n):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        if st:
            pse[i] = st[-1]
        st.append(i)
    return pse

def maxRectangle(arr):
    nse = nextSmallestElement(arr)
    pse = prevSmallestElement(arr)
    area = 0
    for i in range(len(arr)):
        area = max(area, arr[i] * (nse[i] - pse[i] - 1))
    return area

def maximalRectangle(matrix):
    for j in range(len(matrix[0])):
        for i in range(1, len(matrix)):
            if int(matrix[i - 1][j]) == 0 or int(matrix[i][j]) == 0:
                matrix[i][j] = int(matrix[i][j])
            else:
                matrix[i][j] = int(matrix[i][j]) + int(matrix[i - 1][j])
    for j in range(len(matrix[0])):
        matrix[0][j] = int(matrix[0][j])
    area = 0
    for row in matrix:
        area = max(area, maxRectangle(row))
    return area
