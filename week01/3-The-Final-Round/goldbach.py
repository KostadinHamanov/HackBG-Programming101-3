def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def goldbach(n):
    result = []
    if n > 2 and n % 2 == 0:
        for divisor in range(2, n // 2 + 1):
            if is_prime(divisor) and is_prime(n - divisor):
                result.append((divisor, n - divisor))

    return result


def main():
    print (goldbach(4))
    print (goldbach(6))
    print (goldbach(8))
    print (goldbach(10))
    print (goldbach(100))

if __name__ == "__main__":
    main()
