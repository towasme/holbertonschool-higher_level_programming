#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        for i in range(len(my_list)):
            if i == idx:
                if 0 <= idx < len(my_list):
                    del my_list[idx]
                else:
                    continue
        return (my_list)
