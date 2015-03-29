def unique_words_count(arr):
    count = 0
    words = {}
    for word in arr:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

    for word in words.keys():
        if words[word] >= 1:
            count += 1

    return count


def main():
    print (unique_words_count(["apple", "banana", "apple", "pie"]))
    print (unique_words_count(["python", "python", "python", "ruby"]))
    print (unique_words_count(["HELLO!"] * 10))

if __name__ == "__main__":
    main()
