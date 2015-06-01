def count_words(arr):
    words = {}
    for word in arr:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

    return words


def main():
    print (count_words(["apple", "banana", "apple", "pie"]))
    print (count_words(["python", "python", "python", "ruby"]))

if __name__ == "__main__":
    main()
