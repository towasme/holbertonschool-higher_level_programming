#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    j = 0
    for i in range(list_length):
        try:
            num = (my_list_1[j] / my_list_2[j])
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except TypeError:
            print("wrong type")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            new_list[j] = num
            j += 1
    return new_list
