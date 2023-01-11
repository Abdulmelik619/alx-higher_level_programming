#!/usr/bin/python3
"""something is written here"""

def read_file(filename=""):
	with open(filename,encoding="utf-8") as f:
		print(f.read())
