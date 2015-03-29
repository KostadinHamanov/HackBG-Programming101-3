def to_number(digits):
    result = [str(x) for x in digits]
    str_result = "".join(result)

    return str_result


def main():
    print (to_number([1, 2, 3]))
    print (to_number([9, 9, 9, 9, 9]))
    print (to_number([1, 2, 3, 0, 2, 3]))

if __name__ == "__main__":
    main()
