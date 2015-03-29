def count_substrings(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    pos = count = 0

    while(pos < haystack_len - needle_len + 1):
        if haystack[pos: pos + needle_len] == needle:
            count += 1
            pos += needle_len
        else:
            pos += 1
    return count


def main():
    print (count_substrings("This is a test string", "is"))
    print (count_substrings("babababa", "baba"))
    print (count_substrings("Python is an awesome language to program in!", "o"))
    print (count_substrings("We have nothing in common!", "really?"))
    print (count_substrings("This is this and that is this", "this"))

if __name__ == "__main__":
    main()
