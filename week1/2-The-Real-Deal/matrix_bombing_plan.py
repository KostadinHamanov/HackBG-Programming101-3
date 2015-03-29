import copy
import pprint


def sum_position(row, col, bomb, m):

    if m[row][col] >= bomb:
        return m[row][col] - bomb
    else:
        return 0


def big_boombing(matrix, row, col):
    m = copy.deepcopy(matrix)
    total_sum = 0
    bomb = m[row][col]

    if row + 1 < len(m):
        m[row + 1][col] = sum_position(row + 1, col, bomb, m)

    if row - 1 >= 0:
        m[row - 1][col] = sum_position(row - 1, col, bomb, m)

    if col + 1 < len(m[row]):
        m[row][col + 1] = sum_position(row, col + 1, bomb, m)

    if col - 1 >= 0:
        m[row][col - 1] = sum_position(row, col - 1, bomb, m)

    if row - 1 >= 0 and col - 1 >= 0:
        m[row - 1][col - 1] = sum_position(row - 1, col - 1, bomb, m)

    if row - 1 >= 0 and col + 1 < len(m[row]):
        m[row - 1][col + 1] = sum_position(row - 1, col + 1, bomb, m)

    if row + 1 < len(m) and col - 1 >= 0:
        m[row + 1][col - 1] = sum_position(row + 1, col - 1, bomb, m)

    if row + 1 < len(m) and col + 1 < len(m[row]):
        m[row + 1][col + 1] = sum_position(row + 1, col + 1, bomb, m)

    for row in range(len(m)):
        for col in range(len(m[row])):
            total_sum += m[row][col]

    return total_sum


def matrix_bombing_plan(m):
    result = {}
    for row in range(len(m)):
        for col in range(len(m[row])):
            position = (row, col)
            result[position] = big_boombing(m, row, col)

    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == "__main__":
    main()
