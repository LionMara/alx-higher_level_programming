#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0

    if len(sys.argv) < 2:
        print(0)
    else:
        i = 1
        while i < len(sys.argv):
            sum = sum + int(sys.argv[i])
            i += 1
        print(sum)
