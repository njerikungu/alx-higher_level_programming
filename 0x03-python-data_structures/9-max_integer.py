#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length > 0:
        bigg = my_list[0]
        for num in my_list:
            if num >= bigg:
                bigg = num
                return bigg
            else:
                return None
