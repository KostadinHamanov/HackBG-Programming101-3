# Sum integers from file
import sys


def sum_integers_from_file():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        file_with_nums = open(file_name, "r")

        contents = file_with_nums.read()
        nums = contents.split()
        numbers = [int(num) for num in nums]
        file_with_nums.close()

        return sum(numbers)

    else:
        return "Please enner valid data"


def main():
    print (sum_integers_from_file())

if __name__ == '__main__':
    main()
