#!/usr/bin/python3
def fu(number):
    return True if number not in (101, 113) else False
print(''.join(['{}'.format(chr(i)) for i in range(97, 123) if fu(i)]), end='')
