#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results_list: list = []
    for index in range(list_length):
        result = 0
        try:
            result = my_list_1[index]/my_list_2[index]
        except TypeError as e:
            print("wrong type")
        except ZeroDivisionError as e:
            print("division by 0")
        except IndexError as e:
            print("out of range")
        finally:
            results_list.append(result)
    return results_list
