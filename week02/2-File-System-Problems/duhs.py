# Implement an alternative to du -h command
from os.path import join, getsize
import sys
import os


def size_of_directory():
    if (len(sys.argv)) == 2:
        directory = sys.argv[1]
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(directory):
            for name in filenames:
                fp = join(dirpath, name)
                total_size += getsize(fp)
        return total_size / (1024 * 1024)

    else:
        return "Please enter valid data"


def main():
    print (size_of_directory())

if __name__ == "__main__":
    main()
