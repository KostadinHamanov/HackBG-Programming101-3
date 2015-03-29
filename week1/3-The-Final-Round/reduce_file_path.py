def reduce_file_path(path):
    path = path.split("/")
    newPath = []
    for position in range(len(path)):
        if not path[position] == "" and not path[position] == ".":
            newPath.append(path[position])

    for position in range(len(newPath)):
        if newPath[position] == "..":
            if position - 1 >= 0:
                del newPath[position - 1: len(newPath)]
                break
            else:
                del newPath[position]

    result = ""
    if len(newPath) == 0:
        result += "/"
    else:
        for element in newPath:
            result += "/" + element

    return result


def main():
    print (reduce_file_path("/home//radorado/code/./hackbulgaria/week0/../"))
    print (reduce_file_path("/"))
    print (reduce_file_path("/srv/../"))
    print (reduce_file_path("/srv/www/htdocs/wtf/"))
    print (reduce_file_path("/srv/www/htdocs/wtf"))
    print (reduce_file_path("/srv/./././././"))
    print (reduce_file_path("/etc//wtf/"))
    print (reduce_file_path("/etc/../etc/../etc/../"))
    print (reduce_file_path("//////////////"))
    print (reduce_file_path("/../"))

if __name__ == "__main__":
    main()
