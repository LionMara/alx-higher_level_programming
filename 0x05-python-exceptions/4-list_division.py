#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    switch = 0

    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            switch = 1
        except TypeError:
            print("wrong type")
            switch = 1
        except IndexError:
            print("out of range")
            switch = 1
        finally:
            if switch:
                switch = 0
                final_list.append(0)
            else:
                final_list.append(x)
    return final_list
