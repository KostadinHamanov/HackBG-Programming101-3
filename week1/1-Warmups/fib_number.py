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


def main():
    print (fib_number(3))
    print (fib_number(10))

if __name__ == "__main__":
    main()
