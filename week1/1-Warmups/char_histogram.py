def char_histogram(string):
    histogram = {}
    for letter in string:
        if letter in histogram.keys():
            histogram[letter] += 1
        else:
            histogram[letter] = 1

    return histogram


def main():
    print (char_histogram("Python!"))
    print (char_histogram("AAAAaaa!!!"))

if __name__ == "__main__":
    main()
