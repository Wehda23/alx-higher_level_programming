#!/usr/bin/python3
def get_alphabet(i):
    return chr(i) if i % 2 == 0 else chr(i - 32)


for i in range(122, 96, -1):
    print("{}".format(get_alphabet(i)), end="")
