#!/usr/bin/python3
for number in range(100):
    if number < 10:
        number = "0" + str(number)
    if int(number) < 99:
        print("{}".format(number), end=", ")
    else:
        print("{}".format(number))
