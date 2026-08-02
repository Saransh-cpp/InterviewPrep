def isValidSudoku(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num == ".": continue
            for i in range(9):
                if i != col and board[row][i] == num:
                    return False
                elif i != row and board[i][col] == num:
                    return False
                r = 3 * (row // 3) + i // 3
                c = 3 * (col // 3) + i % 3
                if r != row and c != col and board[r][c] == num:
                    return False
    return True

def isValidSudoku(board):
    rvals = [set() for _ in range(9)]
    cvals = [set() for _ in range(9)]
    bvals = [set() for _ in range(9)]

    for row in range(9):
        for col in range(9):
            block = row // 3 + 3 * (col // 3)
            num = board[row][col]
            if num != ".":
                if (
                    num in rvals[row]
                    or num in cvals[col]
                    or num in bvals[block]
                ):
                    return False
                rvals[row].add(num)
                cvals[col].add(num)
                bvals[block].add(num)
    return True
