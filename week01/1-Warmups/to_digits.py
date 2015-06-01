def to_digits(n):
    return [int(x) for x in str(n)]


def main():
    print (to_digits(123))
    print (to_digits(99999))
    print (to_digits(123023))

if __name__ == "__main__":
    main()
