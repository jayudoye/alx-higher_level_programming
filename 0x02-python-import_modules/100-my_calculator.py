#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num = len(argv) - 1
    if num != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] == '+':
        res = add(int(argv[1]), int(argv[3]))
    elif argv[2] == '-':
        res = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == '*':
        res = mul(int(argv[1]), int(argv[3]))
    elif argv[2] == '/':
        res = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], res))
