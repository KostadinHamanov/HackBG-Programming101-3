# cat.py
# Implementing the cat command - Print file contents
import sys


def print_file_contents():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        contents = text_file.read()
        text_file.close()
        return contents

    else:
        return "Please enter valid data"


def main():
    print (print_file_contents())

if __name__ == '__main__':
    main()
