def sum_matrix(m):
    total_sum = 0

    for row in m:
        for col in row:
            total_sum += col

    return total_sum

# def sum_matrix(matr):
#     result = 0

#     for row in matr:
#         result += sum(row)

#     return result

# def sum_matrix2(matr):
# Using list comprehensions
#     return sum([sum(row) for row in matr])


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print (sum_matrix(m))

    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print (sum_matrix(m))

    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print (sum_matrix(m))

if __name__ == "__main__":
    main()
