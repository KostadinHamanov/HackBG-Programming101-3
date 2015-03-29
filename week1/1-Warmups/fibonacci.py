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


def main():
    print (fibonacci(0))
    print (fibonacci(1))
    print (fibonacci(2))
    print (fibonacci(3))
    print (fibonacci(5))
    print (fibonacci(10))

if __name__ == '__main__':
    main()
