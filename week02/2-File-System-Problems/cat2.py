# cat2.py
# Cat multiple files
import sys


def print_multilpe_files():
    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            filename = sys.argv[arg]
            text_file = open(filename, "r")
            content = text_file.read()
            text_file.close()
            print (content)
    else:
        print ("Please enter valid data")


def main():
    print_multilpe_files()

if __name__ == '__main__':
    main()
