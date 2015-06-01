def nan_expand(times):
    if times < 1:
        return ""
    return "Not a " * times + "NaN"


def main():
    print (nan_expand(0))
    print (nan_expand(1))
    print (nan_expand(2))
    print (nan_expand(3))

if __name__ == "__main__":
    main()
