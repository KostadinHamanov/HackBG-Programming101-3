from datetime import date


def count_words(arr):
    words = {}
    for word in arr:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

    return words


def unique_words_count(arr):
    count = 0
    words = {}
    for word in arr:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

    for word in words.keys():
        if words[word] >= 1:
            count += 1

    return count


def nan_expand(times):
    if times < 1:
        return ""
    return "Not a " * times + "NaN"


def iterations_of_nan_expand(expanded):
    expanded_len = len(expanded)
    string = "Not a "
    string_len = len(string)
    position = count = 0

    if not len(expanded):
        return 0

    while position < expanded_len - string_len + 1:
        if expanded[position: position + string_len] == string:
            count += 1
            position += string_len
        else:
            return False

    if not expanded[position:len(expanded)] == "NaN":
        return False

    return count


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def times(n, divisor):
    times = 0
    while is_prime(divisor) and n % divisor == 0:
        times += 1
        n = n // divisor
    return times


def prime_divisors(n):
    prime_divs = {}
    for divisor in range(1, n + 1):
        t = times(n, divisor)
        if is_prime(divisor) and n % divisor == 0:
            prime_divs[divisor] = t
    return prime_divs


def prime_factorization(n):
    dic = prime_divisors(n)
    result = []
    for key in sorted(dic):
        result.append((key, dic[key]))

    return result


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and items[index] == first:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    grouped = group(items)
    return max(len(array) for array in grouped)


def groupby(func, seq):
    seq.sort()
    result = {}
    for number in seq:
        key = func(number)
        if key in result.keys():
            result[key].append(number)
        else:
            result[key] = [number]

    return result


def prepare_meal(number):
    n = 1
    if number % 3 == 0:
        while number % pow(3, n) == 0:
            n += 1

        result = "spam " * (n - 1)

        if number % 5 == 0:
            result += "and eggs"
            return result
        else:
            return result.strip()

    elif number % 5 == 0:
        return "eggs"
    else:
        return ""


def reduce_file_path(path):
    path = path.split("/")
    newPath = []
    for position in range(len(path)):
        if not path[position] == "" and not path[position] == ".":
            newPath.append(path[position])

    for position in range(len(newPath)):
        if newPath[position] == "..":
            if position - 1 >= 0:
                del newPath[position - 1: len(newPath)]
                break
            else:
                del newPath[position]

    result = ""
    if len(newPath) == 0:
        result += "/"
    else:
        for element in newPath:
            result += "/" + element

    return result


def is_an_bn(word):
    middle = len(word) // 2
    if len(word) % 2 != 0:
        return False

    for position in range(middle):
        if word[position] != "a":
            return False
        if word[len(word) - position - 1] != "b":
            return False

    return True


def is_credit_card_valid(number):
    number = [int(x) for x in str(number)]

    index = 0

    if len(number) % 2 != 0:
        while index < len(number):
            if index % 2 != 0:
                number[index] = number[index] * 2
            index += 1

        str_number = ""
        for position in range(len(number)):
            str_number += str(number[position])

        number = [int(x) for x in str_number]

    return sum(number) % 10 == 0


def goldbach(n):
    result = []
    if n > 2 and n % 2 == 0:
        for divisor in range(2, n // 2 + 1):
            if is_prime(divisor) and is_prime(n - divisor):
                result.append((divisor, n - divisor))

    return result


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


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def friday_years(start, end):
    fridayYears = 0

    for year in range(start, end + 1):
        if is_leap(year):
            if (date(year, 1, 1).isoweekday() == 5) or \
                    (date(year, 1, 2).isoweekday() == 5):

                fridayYears += 1
        else:
            if (date(year, 1, 1).isoweekday() == 5):
                fridayYears += 1
    return fridayYears
