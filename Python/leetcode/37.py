def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    recurse(board)

def recurse(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for num in range(1, 10):
                    if is_possible(board, i, j, f"{num}"):
                        board[i][j] = f"{num}"
                        if recurse(board): return True
                        else: board[i][j] = "."
                return False
    return True

def is_possible(board, row, col, num):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][col] == num:
            return False
    for i in range(3 * (row // 3), (3 * (row // 3)) + 3):
        for j in range(3 * (col // 3), (3 * (col // 3)) + 3):
            if num == board[i][j]:
                return False
    return True

def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    r_elems = [set() for _ in range(9)]
    c_elems = [set() for _ in range(9)]
    b_elems = [set() for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if board[row][col] != ".":
                r_elems[row].add(board[row][col])
                c_elems[col].add(board[row][col])
                b_elems[row // 3 + 3 * (col // 3)].add(board[row][col])
    recurse(board, r_elems, b_elems, c_elems)

def recurse(board, r_elems, b_elems, c_elems):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for num in "123456789":
                    if (
                        num not in r_elems[i]
                        and num not in c_elems[j]
                        and num not in b_elems[i // 3 + 3 * (j // 3)]
                    ):
                        board[i][j] = num
                        r_elems[i].add(num)
                        c_elems[j].add(num)
                        b_elems[i // 3 + 3 * (j // 3)].add(num)
                        if recurse(board, r_elems, b_elems, c_elems):
                            return True
                        else:
                            board[i][j] = "."
                            r_elems[i].remove(num)
                            c_elems[j].remove(num)
                            b_elems[i // 3 + 3 * (j // 3)].remove(num)
                return False
    return True
