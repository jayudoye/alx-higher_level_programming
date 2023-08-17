#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    operators = "+-*/"
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif args[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[0])
    b = int(args[2])
    if args[1] == '+':
        result = add(a, b)
    elif args[1] == '-':
        result = sub(a, b)
    elif args[1] == '*':
        result = mul(a, b)
    else:
        result = div(a, b)

    print("{} {} {} = {}".format(args[0], args[1], args[2], result))
