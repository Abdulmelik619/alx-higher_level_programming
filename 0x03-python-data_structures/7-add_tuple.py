#!/usr/bin/python3
# 7-add_tuple.py
# Brennan D Baraban <@aladkfhnckzxcmdszxk.com>


def add_tuple(tuple_a=(), tuple_b=()):
    t=()
    for x in range(len(tuple_a)-1):
        sum=tuple_a[x]+tuple_b[x]
        t+=(,sum)
