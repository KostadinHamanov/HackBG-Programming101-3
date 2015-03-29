import copy
import pprint


# Sum all divisors of an integer
def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])

# print (sum_of_divisors(8))
# print (sum_of_divisors(7))
# print (sum_of_divisors(1))
# print (sum_of_divisors(1000))


# Check if integer is prime
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

# print (is_prime(0))
# print (is_prime(1))
# print (is_prime(2))
# print (is_prime(8))
# print (is_prime(11))
# print (is_prime(-10))


# Check if a number has a prime number of divisors
def prime_number_of_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1

    if is_prime(divisors):
        return True
    else:
        return False

# print (prime_number_of_divisors(7))
# print (prime_number_of_divisors(8))
# print (prime_number_of_divisors(9))


# def count_of_divisors(n):
#     return sum([1 for x in range(1, n + 1) if n % x == 0])

# def prime_number_of_divisors(n):
#     is_prime(count_of_divisors(n))


# Number containing a single digit?


def contains_digit(number, digit):
    list_number = list(str(number))
    for item in list_number:
        if int(item) == digit:
            return True
    return False

#   return digit in to_digits(number)

# print (contains_digit(123, 4))
# print (contains_digit(42, 2))
# print (contains_digit(1000, 0))
# print (contains_digit(12346789, 5))


# Number containing all digits?

def contains_digits(number, digits):
    for i in range(len(digits)):
        if not contains_digit(number, digits[i]):
            return False
    return True

    # for digit in digits:
    #     if not contains_digit(number, digit):
    #         return False

    # return True

# print (contains_digits(402123, [0, 3, 4]))
# print (contains_digits(666, [6, 4]))
# print (contains_digits(123456789, [1, 2, 3, 0]))
# print (contains_digits(456, []))


# Is number balanced?


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

# print (is_number_balanced(9))
# print (is_number_balanced(11))
# print (is_number_balanced(13))
# print (is_number_balanced(121))
# print (is_number_balanced(4518))
# print (is_number_balanced(28471))
# print (is_number_balanced(1238033))


# Counting substrings

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

# print (count_substrings("This is a test string", "is"))
# print (count_substrings("babababa", "baba"))
# print (count_substrings("Python is an awesome language to program in!", "o"))
# print (count_substrings("We have nothing in common!", "really?"))
# print (count_substrings("This is this and that is this", "this"))


def to_digits(n):
    return [int(x) for x in str(n)]


def to_number(digits):
    result = [str(x) for x in digits]
    str_result = "".join(result)

    return str_result

# Zero Insertion


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

# print (zero_insert(116457))
# print (zero_insert(55555555))
# print (zero_insert(1))
# print (zero_insert(6446))


# Sum Numbers in Matrix

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

# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print (sum_matrix(m))

# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print (sum_matrix(m))

# m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# print (sum_matrix(m))


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
