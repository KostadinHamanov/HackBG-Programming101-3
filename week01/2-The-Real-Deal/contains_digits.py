from contains_digit import contains_digit


def contains_digits(number, digits):
    for i in range(len(digits)):
        if not contains_digit(number, digits[i]):
            return False
    return True


def main():
    print (contains_digits(402123, [0, 3, 4]))
    print (contains_digits(666, [6, 4]))
    print (contains_digits(123456789, [1, 2, 3, 0]))
    print (contains_digits(456, []))

if __name__ == "__main__":
    main()
