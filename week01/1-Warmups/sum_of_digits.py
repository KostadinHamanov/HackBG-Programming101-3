def sum_of_digits(n):
    total_sum = 0

    if n < 0:
        n = abs(n)

    while n > 0:
        total_sum += n % 10
        n = n // 10

    return total_sum


def main():
    print (sum_of_digits(1325132435356))
    print (sum_of_digits(123))
    print (sum_of_digits(6))
    print (sum_of_digits(-10))
    print (sum_of_digits(0))

if __name__ == '__main__':
    main()
