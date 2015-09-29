def set_zero(matrix):
    i_max = len(matrix)
    j_max = len(matrix[0])
    found = []
    for i in range(i_max):
        for k in range(j_max):
            if matrix[i][k] == 0:
                found.append([i, k])
    if found:
        for i in range(len(found)):
            for k in range(j_max):
                for l in range(i_max):
                    matrix[found[i][0]][k] = 0
                    matrix[l][found[i][1]] = 0
        print(matrix)
# Time Limit Exceeded


def efficiend_setZeroes(self, matrix):
    row = len(matrix)
    if row == 0:
        return -1
    col = len(matrix[0])
    if col == 0:
        return -1
    fc0 = False
    fr0 = False
    for i in range(col):
        if matrix[0][i] == 0:
            fr0 = True
    for i in range(row):
        if matrix[i][0] == 0:
            fc0 = True
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, col):
        if matrix[0][i] == 0:
            for j in range(row):
                matrix[j][i] = 0
    for i in range(1, row):
        if matrix[i][0] == 0:
            for j in range(col):
                matrix[i][j] = 0
    if fr0:
        for i in range(col):
            matrix[0][i] = 0
    if fc0:
        for i in range(row):
            matrix[i][0] = 0


a = [[0, 0], [1, 0]]
#a=[[1, 0, 3], [8, 0, 4], [7, 6, 5]]
#a=[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21,8], [13, 12, 11, 10, 9]]
set_zero(a)
