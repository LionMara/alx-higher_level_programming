#!/usr/bin/python3
""" Find Peak"""

def find_peak(list_of_integers):
    n = len(list_of_integers)

    # check if list is empty
    if n == 0:
        return None
    # check if list has only one element
    if n == 1:
        return list_of_integers[0]

    # check if first or lasr element is peak
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n-1] >= list_of_integers[n-2]:
        return list_of_integers[n-1]

    # perfom binary search
    left = 1
    right = n - 2
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid-1] and list_of_integers[mid] >=list_of_integers[mid+1]:
            return list_of_integers[mid]
        elif list_of_integers[mid-1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    # if no peak is found
    return None
