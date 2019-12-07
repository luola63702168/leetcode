def rotate(matrix):
    # print(id(matrix))
    matrix_01 = matrix + []
    # print(id(matrix_01))
    for i in range(len(matrix)):
        matrix_01[i] = [matrix[k][i] for k in range(len(matrix)-1,-1,-1)]
    matrix[:] = matrix_01
    # print(id(matrix))
    return matrix

    # 参考别人的解法，发现是我太局限了
    # matrix[:] = map(list, zip(*matrix[:: -1]))
    # return matrix


if __name__ == '__main__':
    print(rotate([
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]))



