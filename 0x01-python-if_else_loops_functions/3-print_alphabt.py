#!/usr/bin/python3
def func(number):
    return True if number not in (101, 113) else False

print(''.join(['{}'.format(chr(i)) for i in range(97, 123) if func(i)]), end='')
