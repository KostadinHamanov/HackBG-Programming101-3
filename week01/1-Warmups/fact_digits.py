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


def main():
    print (fact_digits(0))
    print (fact_digits(1))
    print (fact_digits(111))
    print (fact_digits(145))
    print (fact_digits(-999))

if __name__ == '__main__':
    main()
