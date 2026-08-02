def exist(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if recurse(board, 1, word, row, col, word[0], {(row, col)}):
                    return True
    return False

def recurse(board, ind, word, row, col, curr, s):
    if curr == word:
        return True
    if ind > len(word) - 1:
        return False
    if (
        col < len(board[0]) - 1
        and board[row][col + 1] == word[ind]
        and (row, col + 1) not in s
    ):
        s.add((row, col + 1))
        if recurse(board, ind + 1, word, row, col + 1, curr + word[ind], s):
            return True
        s.remove((row, col + 1))
    if (
        row < len(board) - 1
        and board[row + 1][col] == word[ind]
        and (row + 1, col) not in s
    ):
        s.add((row + 1, col))
        if recurse(board, ind + 1, word, row + 1, col, curr + word[ind], s):
            return True
        s.remove((row + 1, col))
    if (
        col > 0
        and board[row][col - 1] == word[ind]
        and (row, col - 1) not in s
    ):
        s.add((row, col - 1))
        if recurse(board, ind + 1, word, row, col - 1, curr + word[ind], s):
            return True
        s.remove((row, col - 1))
    if (
        row > 0
        and board[row - 1][col] == word[ind]
        and (row - 1, col) not in s
    ):
        s.add((row - 1, col))
        if recurse(board, ind + 1, word, row - 1, col, curr + word[ind], s):
            return True
        s.remove((row - 1, col))
    return False

def exist(board, word):
    if board[0][0] == word: return True

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if recurse(board, 0, row, col, word):
                    return True
    return False

def recurse(board, ind, row, col, word):
    if ind == len(word):
        return True
    if board[row][col] == "." or board[row][col] != word[ind]:
        return False
    char = board[row][col]
    board[row][col] = "."
    if (
        col < len(board[0]) - 1
        and recurse(board, ind + 1, row, col + 1, word)
    ):
        return True
    if (
        row < len(board) - 1
        and recurse(board, ind + 1, row + 1, col, word)
    ):
        return True
    if (
        col > 0
        and recurse(board, ind + 1, row, col - 1, word)
    ):
        return True
    if (
        row > 0
        and recurse(board, ind + 1, row - 1, col, word)
    ):
        return True
    board[row][col] = char
    return False

