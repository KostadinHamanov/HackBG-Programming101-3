def is_an_bn(word):
    middle = len(word) // 2
    if len(word) % 2 != 0:
        return False

    for position in range(middle):
        if word[position] != "a":
            return False
        if word[len(word) - position - 1] != "b":
            return False

    return True


def main():
    print (is_an_bn(""))
    print (is_an_bn("rado"))
    print (is_an_bn("aaabb"))
    print (is_an_bn("aaabbb"))
    print (is_an_bn("aabbaabb"))
    print (is_an_bn("bbbaaa"))
    print (is_an_bn("aaaaabbbbb"))

if __name__ == "__main__":
    main()
