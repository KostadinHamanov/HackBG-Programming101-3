def to_digits(n):
    list_of_digits = []
    number = str(n)
    for digit in number:
        list_of_digits.append(digit)

    return list_of_digits


def main():
    print (to_digits(123))
    print (to_digits(99999))
    print (to_digits(123023))

if __name__ == "__main__":
    main()
