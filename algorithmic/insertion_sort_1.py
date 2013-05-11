#!/bin/python

# Head ends here
def insertionSort(ar):
    v = ar[-1]
    index = 0
    for i in reversed(range(len(ar) - 1)):
        if ar[i] > v:
            ar[i + 1] = ar[i]
        else:
            index = i + 1
            break
        
        print ' '.join(str(n) for n in ar)
    
    ar[index] = v
    print ' '.join(str(n) for n in ar)
    return ""

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)