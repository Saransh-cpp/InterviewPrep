def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]
    recurse(board, res, 0)
    return res

def recurse(board, res, row):
    if row == len(board):
        res.append(["".join(r) for r in board])
        return

    for i in range(len(board)):
        if is_possible(board, row, i):
            board[row][i] = "Q"
            recurse(board, res, row + 1)
            board[row][i] = "."

def is_possible(board, row, col):
    i = row
    while i >= 0:
        if board[i][col] == "Q":
            return False
        i -= 1
    
    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    return True
