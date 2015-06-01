def palindrome(obj):

    obj = str(obj)

    rev = obj[::-1]

    if rev == obj:
        return True
    else:
        return False


def main():
    print (palindrome(121))
    print (palindrome("kapak"))
    print (palindrome("baba"))

if __name__ == '__main__':
    main()
