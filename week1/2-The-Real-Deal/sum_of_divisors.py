def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def main():
    print (sum_of_divisors(8))
    print (sum_of_divisors(7))
    print (sum_of_divisors(1))
    print (sum_of_divisors(1000))

if __name__ == "__main__":
    main()
