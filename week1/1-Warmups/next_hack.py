def is_hack_num(n):
    isHack = True
    isPalindrome = False
    binNum = bin(n)[2:]

    if binNum == binNum[::-1]:
        isPalindrome = True

    if not isPalindrome:
        isHack = False

    onesCount = 0

    for digit in binNum:
        if digit == "1":
            onesCount += 1

    if onesCount % 2 == 0:
        isHack = False

    return isHack


def next_hack(n):
    n += 1
    while not is_hack_num(n):
        n += 1

    return n


def main():
    print (next_hack(0))
    print (next_hack(10))
    print (next_hack(8031))

if __name__ == "__main__":
    main()
