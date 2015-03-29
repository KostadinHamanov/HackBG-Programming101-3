def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    print (factorial(-10))
    print (factorial(-1))
    print (factorial(0))
    print (factorial(1))
    print (factorial(2))
    print (factorial(5))
    print (factorial(7))

if __name__ == '__main__':
    main()
