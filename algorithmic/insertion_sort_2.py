#!/bin/python

# Head ends here
def insertionSort(ar):
    cursor = 1
    while cursor < len(ar):
        for i in reversed(range(cursor)):
            v = ar[i]
            if ar[i + 1] < v:
                ar[i] = ar[i + 1]
                ar[i + 1] = v
            else:
                break

        print ' '.join(str(n) for n in ar)
        cursor = cursor + 1
    
    return ""

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)