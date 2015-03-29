def iterations_of_nan_expand(expanded):
    expanded_len = len(expanded)
    string = "Not a "
    string_len = len(string)
    position = count = 0

    if not len(expanded):
        return 0

    while position < expanded_len - string_len + 1:
        if expanded[position: position + string_len] == string:
            count += 1
            position += string_len
        else:
            return False

    if not expanded[position:len(expanded)] == "NaN":
        return False

    return count


def main():
    print (iterations_of_nan_expand(""))
    print (iterations_of_nan_expand("Not a NaN   "))
    print (iterations_of_nan_expand("Not a NaN"))
    print (iterations_of_nan_expand
           ('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    print (iterations_of_nan_expand("Show these people!"))

if __name__ == "__main__":
    main()
