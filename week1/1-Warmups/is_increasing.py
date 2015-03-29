def is_increasing(seq):

    is_incr = True
    length = len(seq)

    if length < 1:
        is_incr = False
    else:
        previous = seq[0]
        for current in range(1, length):
            if int(seq[current]) <= int(previous):
                is_incr = False
            else:
                previous = int(seq[current])

    return is_incr


def main():
    print (is_increasing([1, 2, 3, 4, 5]))
    print (is_increasing([1]))
    print (is_increasing([5, 6, -10]))
    print (is_increasing([1, 1, 1, 1]))
    print (is_increasing([]))

if __name__ == "__main__":
    main()
