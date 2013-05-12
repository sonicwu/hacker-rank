#!/bin/python

# Head ends here
def insertionSort(ar):
    running_time = 0

    cursor = 1
    while cursor < len(ar):
        for i in reversed(range(cursor)):
            v = ar[i]
            if ar[i + 1] < v:
                ar[i] = ar[i + 1]
                ar[i + 1] = v
                running_time += 1
            else:
                break

        cursor += 1
    
    print running_time
    return ""

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)