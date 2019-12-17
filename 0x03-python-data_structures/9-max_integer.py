#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        cont = my_list[0]
        for i in range(len(my_list)):
            if cont < my_list[i]:
                cont = my_list[i]
        return (cont)
    return ("None")
