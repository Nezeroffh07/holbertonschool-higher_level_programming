#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))

    if count >= 1:
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
