# Factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# print (factorial(-10))
# print (factorial(-1))
# print (factorial(0))
# print (factorial(1))
# print (factorial(2))
# print (factorial(5))
# print (factorial(7))


# First nth members of Fibonacci

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

# print (fibonacci(0))
# print (fibonacci(1))
# print (fibonacci(2))
# print (fibonacci(3))
# print (fibonacci(5))
# print (fibonacci(10))


# Sum all digits of a number

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

# print (sum_of_digits(1325132435356))
# print (sum_of_digits(123))
# print (sum_of_digits(6))
# print (sum_of_digits(-10))
# print (sum_of_digits(0))


# Factorial Digits

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

# print (fact_digits(0))
# print (fact_digits(1))
# print (fact_digits(111))
# print (fact_digits(145))
# print (fact_digits(-999))


# Palindrome

def palindrome(obj):

    obj = str(obj)

    rev = obj[::-1]

    if rev == obj:
        return True
    else:
        return False

# print (palindrome(121))
# print (palindrome("kapak"))
# print (palindrome("baba"))


# Turn a number into a list of digits

def to_digits(n):
    list_of_digits = []
    number = str(n)
    for digit in number:
        list_of_digits.append(digit)

    return list_of_digits

# print (to_digits(123))
# print (to_digits(99999))
# print (to_digits(123023))


# Turn a list of digits into a number

def to_number(digits):
    result = [str(x) for x in digits]
    str_result = "".join(result)

    return str_result

# print (to_number([1, 2, 3]))
# print (to_number([9, 9, 9, 9, 9]))
# print (to_number([1, 2, 3, 0, 2, 3]))


# Fibonacci number

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

    return result

# print (fib_number(3))
# print (fib_number(10))


# Vowels in a string

def count_vowels(str):
    count = 0
    for a in str:
        for i in "aeiouyAEIOUY":
            if a == i:
                count += 1

    return count

# print (count_vowels("Python"))
# print (count_vowels("Theistareykjarbunga"))
# print (count_vowels("grrrrgh!"))
# print (count_vowels
#        ("Github is the second best thing that \
#         happend to programmers, after the keyboard!"))
# print (count_vowels("A nice day to code!"))


# Consonants in a string

def count_consonants(str):
    count = 0
    new_str = str.lower()
    for a in new_str:
        for i in "bcdfghjklmnpqrstvwxz":
            if a == i:
                count += 1

    return count

# print (count_consonants("Python"))
# print (count_consonants("Theistareykjarbunga"))
# print (count_consonants("grrrrgh!"))
# print (count_consonants("Github is the second best \
#     thing that happend to programmers, after the keyboard!"))
# print (count_consonants("A nice day to code!"))


# Char Histogram

def char_histogram(string):
    histogram = {}
    for letter in string:
        if letter in histogram.keys():
            histogram[letter] += 1
        else:
            histogram[letter] = 1

    return histogram

# print (char_histogram("Python!"))
# print (char_histogram("AAAAaaa!!!"))


# Palindrome Score

def p_score(n):
    digits = str(n)
    if digits == digits[::-1]:
        return 1

    s = n + int(digits[::-1])

    return 1 + p_score(s)


# print (p_score(121))
# print (p_score(48))
# print (p_score(198))


# Increasing sequence?

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

# print (is_increasing([1, 2, 3, 4, 5]))
# print (is_increasing([1]))
# print (is_increasing([5, 6, -10]))
# print (is_increasing([1, 1, 1, 1]))
# print (is_increasing([]))


# Descreasing sequence?

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

# print (is_decreasing([5, 4, 3, 2, 1]))
# print (is_decreasing([1, 2, 3]))
# print (is_decreasing([100, 50, 20]))
# print (is_decreasing([1, 1, 1, 1]))


# Hack Numbers

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


# print (next_hack(0))
# print (next_hack(10))
# print (next_hack(8031))
