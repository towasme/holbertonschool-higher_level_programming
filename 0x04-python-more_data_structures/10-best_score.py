#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        max_key = set()
        max_key = a_dictionary.copy()
        max_key.sort()
        return (max_key[-1])
    return ("None")
