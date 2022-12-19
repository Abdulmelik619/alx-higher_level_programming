def safe_print_list(my_list=[], x=0):
    try:
        sum=0
        for y in range(x):
            print(my_list[y],end="")
            sum+=1
    except:
        continue
    print()
    return sum

