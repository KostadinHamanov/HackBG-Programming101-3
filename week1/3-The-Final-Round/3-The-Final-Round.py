from datetime import date

# Count words


def count_words(arr):
    words = {}
    for word in arr:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

    return words

# print (count_words(["apple", "banana", "apple", "pie"]))
# print (count_words(["python", "python", "python", "ruby"]))

# Unique words


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

# print (unique_words_count(["apple", "banana", "apple", "pie"]))
# print (unique_words_count(["python", "python", "python", "ruby"]))
# print (unique_words_count(["HELLO!"] * 10))

# NaN Expand


def nan_expand(times):
    if times < 1:
        return ""
    return "Not a " * times + "NaN"

# print (nan_expand(0))
# print (nan_expand(1))
# print (nan_expand(2))
# print (nan_expand(3))

# Iterations of NaN Expand


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

# print (iterations_of_nan_expand(""))
# print (iterations_of_nan_expand("Not a NaN   "))
# print (iterations_of_nan_expand("Not a NaN"))
# print (iterations_of_nan_expand
#        ('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
# print (iterations_of_nan_expand("Show these people!"))

# Integer prime factorization


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

# print (prime_factorization(10))
# print (prime_factorization(14))
# print (prime_factorization(356))
# print (prime_factorization(89))
# print (prime_factorization(1000))

# The group function


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

# print (group([1, 1, 1, 2, 3, 1, 1]))
# print (group([1, 2, 1, 2, 3, 3]))

# Longest subsequence of equal consecutive elements


def max_consecutive(items):
    grouped = group(items)
    return max(len(array) for array in grouped)

# print (max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print (max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))

# Group By


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

# print (groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
# print (groupby(lambda x: 'odd' if x % 2 else 'even',
#                [1, 2, 3, 5, 8, 9, 10, 12]))
# print (groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))


# Spam and Eggs


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

# print (prepare_meal(5))
# print (prepare_meal(3))
# print (prepare_meal(27))
# print (prepare_meal(15))
# print (prepare_meal(45))
# print (prepare_meal(7))

# Reduce file path


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

# print (reduce_file_path("/home//radorado/code/./hackbulgaria/week0/../"))
# print (reduce_file_path("/"))
# print (reduce_file_path("/srv/../"))
# print (reduce_file_path("/srv/www/htdocs/wtf/"))
# print (reduce_file_path("/srv/www/htdocs/wtf"))
# print (reduce_file_path("/srv/./././././"))
# print (reduce_file_path("/etc//wtf/"))
# print (reduce_file_path("/etc/../etc/../etc/../"))
# print (reduce_file_path("//////////////"))
# print (reduce_file_path("/../"))

# Word from a^nb^n


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

# print (is_an_bn(""))
# print (is_an_bn("rado"))
# print (is_an_bn("aaabb"))
# print (is_an_bn("aaabbb"))
# print (is_an_bn("aabbaabb"))
# print (is_an_bn("bbbaaa"))
# print (is_an_bn("aaaaabbbbb"))

# Credit card validation


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


# print (is_credit_card_valid(79927398713))
# print (is_credit_card_valid(79927398715))


# Goldbach Conjecture


def goldbach(n):
    result = []
    if n > 2 and n % 2 == 0:
        for divisor in range(2, n // 2 + 1):
            if is_prime(divisor) and is_prime(n - divisor):
                result.append((divisor, n - divisor))

    return result

# print (goldbach(4))
# print (goldbach(6))
# print (goldbach(8))
# print (goldbach(10))
# print (goldbach(100))


# Magic Square


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

# print (magic_square([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]]))

# print (magic_square([[4, 9, 2],
#                      [3, 5, 7],
#                      [8, 1, 6]]))

# print (magic_square([[7, 12, 1, 14],
#                      [2, 13, 8, 11],
#                      [16, 3, 10, 5],
#                      [9, 6, 15, 4]]))

# print (magic_square([[23, 28, 21],
#                      [22, 24, 26],
#                      [27, 20, 25]]))

# print (magic_square([[16, 23, 17],
#                      [78, 32, 21],
#                      [17, 16, 15]]))

# Friday Years


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

# print (friday_years(1000, 2000))
# print (friday_years(1753, 2000))
# print (friday_years(1990, 2015))
