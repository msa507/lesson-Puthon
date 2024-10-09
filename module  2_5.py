def get_matrix(n, m, val):
    matrix = []
    for i in range(n):
        matrix.append([val]*m)
    print(matrix)

matrix_1 = [2, 2, 20]
matrix_2 = [3, 5, 42]
matrix_3 = [4, 2, 13]
for i in (matrix_1, matrix_2, matrix_3):
    n = i[0]
    m = i[1]
    val = i[2]
    get_matrix(n, m, val)
