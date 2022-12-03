#!/usr/bin/python3
if __name__=="__main__":
    import hidden_4.pyc
    a=sorted(dir(hidden_4.pyc))
    for name in a:
        if(name[:2]=="__"):
            continue
        print("{:s}".format(name))
