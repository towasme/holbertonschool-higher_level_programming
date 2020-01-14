#!/usr/bin/python3


"""
text_indentation module
function that prints a text with 2 new lines after som specific characters
"""


def text_indentation(text):
    """
    Parameters:
        text: the text the function will recive and then partitionate.
    return:
        print new text partitionate with new lines
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
#   #print the string
    for j in range(len(text)):
        if text[j] is '.' or text[j] is '?' or text[j] is ':':
            print(text[j])
            print()
            j += 1
        elif text[j] == ' ' and text[j - 1] is '.' or \
                text[j - 1] is '?' or text[j - 1] is ':':
                continue
        else:
            print(text[j], end="")
