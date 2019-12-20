#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for j, i in a_dictionary.items():
        new_dic[j] = i * 2
    return (new_dic)
