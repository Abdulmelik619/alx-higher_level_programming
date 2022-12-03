#!/usr/bin/python3
# 1-element_at.py
# Brennan D Baraban <375@holbertonschool.com>

def element_at(my_list, idx):
    """Retrive an element from a list."""
    if(len(my_list)<=0):
        return None
    elif(idx > len(my_list)-1):
        return None
    else:
        return(my_list[idx])
