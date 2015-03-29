def prepare_meal(number):
    n = 1
    if number % 3 == 0:
        while number % pow(3, n) == 0:
            n += 1

        result = "spam " * (n - 1)

        if number % 5 == 0:
            result += "and eggs"
            return result
        else:
            return result.strip()

    elif number % 5 == 0:
        return "eggs"
    else:
        return ""


def main():
    print (prepare_meal(5))
    print (prepare_meal(3))
    print (prepare_meal(27))
    print (prepare_meal(15))
    print (prepare_meal(45))
    print (prepare_meal(7))

if __name__ == "__main__":
    main()
