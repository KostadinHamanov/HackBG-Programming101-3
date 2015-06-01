def magic_square(matrix):
    mainDiagonal = 0
    secondaryDiagonal = 0
    rowsSum = [0 for i in range(len(matrix))]
    colsSum = [0 for i in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col:
                mainDiagonal += matrix[row][col]
            if row + col == len(matrix) - 1:
                secondaryDiagonal += matrix[row][col]
            colsSum[col] += matrix[row][col]
        rowsSum[row] = sum(matrix[row])

    if mainDiagonal != secondaryDiagonal:
        return False

    for i in range(len(matrix)):
        if rowsSum[i] != colsSum[i]:
            return False

    return True


def main():
    print (magic_square([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]))

    print (magic_square([[4, 9, 2],
                         [3, 5, 7],
                         [8, 1, 6]]))

    print (magic_square([[7, 12, 1, 14],
                         [2, 13, 8, 11],
                         [16, 3, 10, 5],
                         [9, 6, 15, 4]]))

    print (magic_square([[23, 28, 21],
                         [22, 24, 26],
                         [27, 20, 25]]))

    print (magic_square([[16, 23, 17],
                         [78, 32, 21],
                         [17, 16, 15]]))

if __name__ == "__main__":
    main()
