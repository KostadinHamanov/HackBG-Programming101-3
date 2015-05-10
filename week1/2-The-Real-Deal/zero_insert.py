def to_digits(n):
    return [int(x) for x in str(n)]


def to_number(digits):
    result = [str(x) for x in digits]
    str_result = "".join(result)

    return int(str_result)

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


def main():
    print (zero_insert(116457))
    print (zero_insert(55555555))
    print (zero_insert(1))
    print (zero_insert(6446))

if __name__ == "__main__":
    main()
