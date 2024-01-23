#!/usr/bin/python3
for n in reversed(range(ord('a'), ord('{'))):
    if n % 2 == 1:
        n -= ord(' ')
    print("{:c}".format(n), end="")
