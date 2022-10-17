#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        instance = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                instance += 1
                print("{:d}".format(my_list[i]), end="")
    except TypeError as err:
        print(err)
    else:
        print("")
        return instance
