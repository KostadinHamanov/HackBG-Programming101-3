# Generating file with random integers
import sys
from random import randint


def generate_random_numbers():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        count_of_numbers = int(sys.argv[2])
        file_with_numbers = open(filename, "w")

        for i in range(0, count_of_numbers):
            file_with_numbers.write(str(randint(1, 1000)))
            file_with_numbers.write(" ")
        file_with_numbers.close()

    else:
        print ("Please enter valid data")


def main():
    generate_random_numbers()


if __name__ == '__main__':
    main()
