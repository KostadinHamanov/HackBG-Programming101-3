import copy
import pprint


def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# return n + 1 == sum_of_divisors(n)


def prime_number_of_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1

    if is_prime(divisors):
        return True
    else:
        return False

# def count_of_divisors(n):
#     return sum([1 for x in range(1, n + 1) if n % x == 0])

# def prime_number_of_divisors(n):
#     is_prime(count_of_divisors(n))


def contains_digit(number, digit):
    list_number = list(str(number))
    for item in list_number:
        if int(item) == digit:
            return True
    return False

#   return digit in to_digits(number)


def contains_digits(number, digits):
    for i in range(len(digits)):
        if not contains_digit(number, digits[i]):
            return False
    return True

    # for digit in digits:
    #     if not contains_digit(number, digit):
    #         return False

    # return True


def is_number_balanced(n):
    if n < 10:
        return True

    digits = list(str(n))
    length = len(str(n))
    sumLeft = sumRight = 0

    for i in range(0, length // 2):
        sumLeft += int(digits[i])
        sumRight += int(digits[length - i - 1])

    if sumLeft == sumRight:
        return True
    else:
        return False

# def is_number_balanced(n):
#     numbs = to_digits(n)
#     half = len(numbs) // 2

#     left_numbs = numbs[0:half]
#     if len(numbs) % 2 == 0:
#         right_numbs = numbs[half:]
#     else:
#         right_numbs = numbs[half + 1:]

#     return sum(left_numbs) == sum(right_numbs)


def count_substrings(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    pos = count = 0

    while(pos < haystack_len - needle_len + 1):
        if haystack[pos: pos + needle_len] == needle:
            count += 1
            pos += needle_len
        else:
            pos += 1
    return count

    # return haystack.count(needle)


def to_digits(n):
    return [int(x) for x in str(n)]


def to_number(digits):
    result = [str(x) for x in digits]
    str_result = "".join(result)

    return int(str_result)


def zero_insert(n):
    result = []

    digits = to_digits(n)

    start = 0
    end = len(digits)

    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]

        result.append(x)

        if (x + y) % 10 == 0 or x == y:
            result.append(0)

        start += 1

    result.append(digits[start])

    return to_number(result)


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
    # return sum([sum(row) for row in matr])


# Matrix Bombing
def sum_position(row, col, bomb, m):

    if m[row][col] >= bomb:
        return m[row][col] - bomb
    else:
        return 0


def big_boombing(mm, row, col):
    m = copy.deepcopy(mm)
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

# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = matrix_bombing_plan(m)

# pp = pprint.PrettyPrinter()
# pp.pprint(result)
