#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, dub, mul, div
    from sys import argv, exit

    argc = len(argv)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if argv != 4:
        print("Usage: {} {} {} {}".format(argv[0], a, op, b))
        exit(1)

    if op == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif op == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif op == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif op == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
