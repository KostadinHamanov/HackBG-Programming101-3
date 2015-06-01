def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and items[index] == first:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def main():
    print (group([1, 1, 1, 2, 3, 1, 1]))
    print (group([1, 2, 1, 2, 3, 3]))

if __name__ == "__main__":
    main()
