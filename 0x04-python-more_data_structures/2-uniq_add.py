#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum=0
    my_list_2=[]
    for x in my_list:
        if(x in my_list):
            continue
        my_list_2.append(x)
    for t in my_list_2:
        sum+=t
    return sum
