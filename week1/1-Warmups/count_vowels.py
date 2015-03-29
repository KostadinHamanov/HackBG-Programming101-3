def count_vowels(str):
    count = 0
    for a in str:
        for i in "aeiouyAEIOUY":
            if a == i:
                count += 1

    return count


def main():
    print (count_vowels("Python"))
    print (count_vowels("Theistareykjarbunga"))
    print (count_vowels("grrrrgh!"))
    print (count_vowels
           ("Github is the second best thing that \
            happend to programmers, after the keyboard!"))
    print (count_vowels("A nice day to code!"))

if __name__ == "__main__":
    main()
