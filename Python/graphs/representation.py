def matrix_to_list(mat, is_zero_based):
    lst = [set() for _ in range(len(mat))] if is_zero_based else [set() for _ in range(len(mat) + 1)]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1 and i != j:
                lst[i].add(j)
                lst[i].add(i)
    return lst


if __name__ == "__main__":
    adj_mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(matrix_to_list(adj_mat, True))
