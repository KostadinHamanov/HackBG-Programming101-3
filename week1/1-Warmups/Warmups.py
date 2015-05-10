def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    fibonacci_list = []

    first = second = 1

    for i in range(1, n + 1):
        if i < 3:
            fibonacci_list.append(1)
        else:
            temp = first + second
            first = second
            second = temp
            fibonacci_list.append(temp)

    return fibonacci_list

# def fibonacci(n):
#     result = []
#     a = 1
#     b = 1
#     while len(result) < n:
#         result.append(a)
#         next_fib = a + b
#         a = b
#         b = next_fib

# return result


def sum_of_digits(n):
    total_sum = 0

    if n < 0:
        n = abs(n)

    while n > 0:
        total_sum += n % 10
        n = n // 10

    return total_sum

# def sum_of_digits(n):
#     return sum(to_digits(n))

# def to_digits(n):
#     return [int(x) for x in str(n)]


def fact_digits(n):
    fact_sum = 0

    if n < 0:
        n = abs(n)

    while n > 0:
        digit = n % 10

        fact = 1
        for i in range(2, digit + 1):
            fact *= i

        fact_sum += fact
        n = n // 10

    return fact_sum

# def factorial_digits(n):
#     return sum([factorial(x) for x in to_digits(n)])


def palindrome(obj):

    obj = str(obj)

    rev = obj[::-1]

    if rev == obj:
        return True
    else:
        return False


def to_digits(n):
    return [int(x) for x in str(n)]


def to_number(digits):
    result = [str(x) for x in digits]
    str_result = "".join(result)

    return int(str_result)


def fib_number(n):
    fibonacci_list = []

    fir = sec = 1

    for i in range(1, n + 1):
        if i < 3:
            fibonacci_list.append(1)
        else:
            temp = fir + sec
            fir = sec
            sec = temp
            fibonacci_list.append(temp)

    result = ""

    for element in fibonacci_list:
        result += str(element)

    return int(result)


def count_vowels(str):
    count = 0
    for a in str:
        for i in "aeiouyAEIOUY":
            if a == i:
                count += 1

    return count


def count_consonants(str):
    count = 0
    new_str = str.lower()
    for a in new_str:
        for i in "bcdfghjklmnpqrstvwxz":
            if a == i:
                count += 1

    return count


def char_histogram(string):
    histogram = {}
    for letter in string:
        if letter in histogram.keys():
            histogram[letter] += 1
        else:
            histogram[letter] = 1

    return histogram


def p_score(n):
    digits = str(n)
    if digits == digits[::-1]:
        return 1

    s = n + int(digits[::-1])

    return 1 + p_score(s)


def is_increasing(seq):

    is_incr = True
    length = len(seq)

    if length < 1:
        is_incr = False
    else:
        previous = seq[0]
        for current in range(1, length):
            if int(seq[current]) <= int(previous):
                is_incr = False
            else:
                previous = int(seq[current])

    return is_incr


def is_decreasing(seq):

    is_decr = True
    length = len(seq)

    if length < 1:
        is_decr = False
    else:
        previous = seq[0]

        for current in range(1, length):
            if int(seq[current]) >= int(previous):
                is_decr = False
            else:
                previous = int(seq[current])

    return is_decr


def is_hack_num(n):
    isHack = True
    isPalindrome = False
    binNum = bin(n)[2:]

    if binNum == binNum[::-1]:
        isPalindrome = True

    if not isPalindrome:
        isHack = False

    onesCount = 0

    for digit in binNum:
        if digit == "1":
            onesCount += 1

    if onesCount % 2 == 0:
        isHack = False

    return isHack


def next_hack(n):
    n += 1
    while not is_hack_num(n):
        n += 1

    return n
