def is_decreasing(seq):

    is_decr = True
    length = len(seq)

    if length < 1:
        is_decr = False
    else:
        previous = seq[0]

        for current in range(1, length):
            if int(seq[current]) >= int(previous):
                is_decr = False
            else:
                previous = int(seq[current])

    return is_decr


def main():
    print (is_decreasing([5, 4, 3, 2, 1]))
    print (is_decreasing([1, 2, 3]))
    print (is_decreasing([100, 50, 20]))
    print (is_decreasing([1, 1, 1, 1]))

if __name__ == "__main__":
    main()
