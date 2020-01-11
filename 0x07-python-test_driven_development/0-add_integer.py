#!/usr/bin/python3
def add_integer(a, b=98):
	if a == None:
		raise TypeError("a must be a integer")
	if b == None:
		raise TypeError("b must be a integer")
	if type(a) is not int and type(a) is not float:
		raise TypeError("a must be an integer")
	if type(b) is not int and type(a) is not float:
		raise TypeError("b must be an integer")
	return int(a + b)
