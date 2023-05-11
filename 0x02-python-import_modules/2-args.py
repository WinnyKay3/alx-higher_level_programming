#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    size = len(argv) - 1
    ar = "argument" if size == 1 else "arguments"
    dot = "." if size == 0 else ":"
    print("{} {}".format(size, ar + dot))
    for i in range(1, size + 1):
        print("{}: {}".format(i, argv[i]))
