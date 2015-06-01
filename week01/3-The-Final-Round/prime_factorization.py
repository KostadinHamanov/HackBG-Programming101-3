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


def main():
    print (prime_factorization(10))
    print (prime_factorization(14))
    print (prime_factorization(356))
    print (prime_factorization(89))
    print (prime_factorization(1000))

if __name__ == "__main__":
    main()
