#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    list_num = []
    for c in argv:
        list_num += [c]
    result = 0
    for i in range(1, len(list_num)):
        result += int(list_num[i])
    print("{:d}".format(result))
