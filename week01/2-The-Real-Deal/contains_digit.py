def contains_digit(number, digit):
    list_number = list(str(number))
    for item in list_number:
        if int(item) == digit:
            return True
    return False


def main():
    print (contains_digit(123, 4))
    print (contains_digit(42, 2))
    print (contains_digit(1000, 0))
    print (contains_digit(12346789, 5))

if __name__ == "__main__":
    main()
