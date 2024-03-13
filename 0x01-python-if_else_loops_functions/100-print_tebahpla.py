#!/usr/bin/python3
lower = True
for i in range(122, 96, -1):
    print("{c}".format(c=chr(i) if lower else chr(i - 32)), end='')
    lower = not lower
