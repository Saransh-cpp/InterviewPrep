def celebrity(M):
    top = 0
    bottom = len(M) - 1
    while top < bottom:
        if M[top][bottom]:
            top += 1
        elif M[bottom][top]:
            bottom -= 1
        else:
            top += 1
            bottom -= 1

    for x in M[top]:
        if x:
            return -1

    for i in range(len(M)):
        if i != top and not M[i][top]:
            return -1

    return top
