from group import group


def max_consecutive(items):
    grouped = group(items)
    return max(len(array) for array in grouped)


def main():
    print (max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    print (max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))

if __name__ == "__main__":
    main()
