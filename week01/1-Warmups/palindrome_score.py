def p_score(n):
    digits = str(n)
    if digits == digits[::-1]:
        return 1

    s = n + int(digits[::-1])

    return 1 + p_score(s)


def main():
    print (p_score(121))
    print (p_score(48))
    print (p_score(198))

if __name__ == "__main__":
    main()
