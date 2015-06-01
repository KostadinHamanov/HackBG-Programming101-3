def is_number_balanced(n):
    if n < 10:
        return True

    digits = list(str(n))
    length = len(str(n))
    sumLeft = sumRight = 0

    for i in range(0, length // 2):
        sumLeft += int(digits[i])
        sumRight += int(digits[length - i - 1])

    if sumLeft == sumRight:
        return True
    else:
        return False


def main():
    print (is_number_balanced(9))
    print (is_number_balanced(11))
    print (is_number_balanced(13))
    print (is_number_balanced(121))
    print (is_number_balanced(4518))
    print (is_number_balanced(28471))
    print (is_number_balanced(1238033))

if __name__ == "__main__":
    main()
